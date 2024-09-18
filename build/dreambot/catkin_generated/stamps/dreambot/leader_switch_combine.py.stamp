#!/usr/bin/env python3

import rospy
from dreambot.msg import CombinedPathStatus
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from visualization_msgs.msg import Marker
from dreambot_tkinter.msg import BoolInt
import numpy as np
import math

class CombinedPathStatusSubscriber:
    def __init__(self):
        rospy.init_node('leader_switch_combine', anonymous=True)
        self.distance_master = None
        self.forward_slave_goal = None
        self.path = None

        self.status_sub = rospy.Subscriber('/combined_path_status', CombinedPathStatus, self.status_callback)
        self.activate_sub = rospy.Subscriber('/activate_base_station', BoolInt, self.activate_callback, queue_size=20)

        self.node_active = False
        self.path_published = False
        self.combined_path = None
        self.reached_final_waypoint = False
        self.distance_flag = False
        self.distance_to_goal = 0.0
        self.goal_master = [0.0, 0.0]

        self.reached_final_waypoint_slave = False
        self.distance_flag_slave = False
        self.goal_slave = [0.0, 0.0]

        self.master_filter_x = 0.0
        self.master_filter_y = 0.0
        self.slave_filter_x = 0.0
        self.slave_filter_y = 0.0

        # Publishers for master
        self.master_error_x_pub = rospy.Publisher('error_master_x', Float64, queue_size=1)
        self.master_input_linear_x_vel_pub = rospy.Publisher('input_linear_master_x_vel', Float64, queue_size=1)
        self.master_error_y_pub = rospy.Publisher('error_master_y', Float64, queue_size=1)
        self.master_input_linear_y_vel_pub = rospy.Publisher('input_linear_master_y_vel', Float64, queue_size=1)
        self.master_vel_pub = rospy.Publisher('master_cmd_vel', Twist, queue_size=10)
        self.master_goal_marker_pub = rospy.Publisher('master_goal_marker', Marker, queue_size=10)

        # Publishers for slave
        self.slave_error_x_pub = rospy.Publisher('error_slave_x', Float64, queue_size=1)
        self.slave_input_linear_x_vel_pub = rospy.Publisher('input_linear_slave_x_vel', Float64, queue_size=1)
        self.slave_error_y_pub = rospy.Publisher('error_slave_y', Float64, queue_size=1)
        self.slave_input_linear_y_vel_pub = rospy.Publisher('input_linear_slave_y_vel', Float64, queue_size=1)
        self.slave_vel_pub = rospy.Publisher('slave_cmd_vel', Twist, queue_size=10)
        self.slave_goal_marker_pub = rospy.Publisher('slave_goal_marker', Marker, queue_size=10)

    def status_callback(self, msg):
        # Update node status from the message
        self.node_active = msg.node_active
        self.forward_slave_goal = msg.path_published
        self.path = self.format_combined_path(msg.path.x, msg.path.y)

    def format_combined_path(self, x_coords, y_coords):
        if not x_coords or not y_coords:
            rospy.logwarn("Received empty path coordinates.")
            return None

        x_array = np.array(x_coords)
        y_array = np.array(y_coords)
        combined_path = np.column_stack((x_array, y_array))

        return combined_path

    def activate_callback(self, msg):
        self.distance_master = msg.number / 2

    def odom_master_callback(self, msg):
        # Check if node is active before proceeding
        if not self.node_active:
            return

        distance_x = self.master_filter_x
        distance_y = self.master_filter_y
        linear_x_in = msg.twist.twist.linear.x
        linear_y_in = msg.twist.twist.linear.y

        self.update_goal_master(distance_x, distance_y)

        error_x = self.goal_master[0] - distance_x
        error_y = self.goal_master[1] - distance_y
        self.distance_to_goal = math.sqrt(error_x ** 2 + error_y ** 2)

        self.master_error_x_pub.publish(Float64(error_x))
        self.master_error_y_pub.publish(Float64(error_y))
        self.master_input_linear_x_vel_pub.publish(Float64(linear_x_in))
        self.master_input_linear_y_vel_pub.publish(Float64(linear_y_in))

    def update_goal_master(self, distance_x, distance_y):
        # Calculate distance to the end of the path
        if self.path is None:
            rospy.logwarn("Path is not initialized.")
            return

        end_of_path = self.path[-1]
        distance_to_end = math.sqrt((end_of_path[0] - distance_x) ** 2 + (end_of_path[1] - distance_y) ** 2)

        if self.forward_slave_goal and distance_to_end <= self.distance_master:
            rospy.loginfo("Master is within distance_master of the end of the path. Keeping current goal.")
            self.reached_final_waypoint = True
            return

        while not self.reached_final_waypoint and not self.distance_flag:
            if self.count_master >= len(self.path):
                self.reached_final_waypoint = True
                self.goal_master = self.path[-1]
                break

            x_val, y_val = self.path[self.count_master]
            distance_to_point = math.sqrt((x_val - distance_x) ** 2 + (y_val - distance_y) ** 2)

            if distance_to_point >= 0.1:
                self.goal_master = [x_val, y_val]
                self.distance_flag = True
                self.publish_goal_marker(self.goal_master, self.master_goal_marker_pub, "master_goal_marker", 0, (1.0, 0.0, 0.0))
            else:
                self.count_master += 1

        if self.distance_to_goal < 0.1:
            self.distance_flag = False

    def update_goal_slave(self):
        if not self.node_active or self.path is None:
            rospy.logwarn("Node is not active or path is not initialized.")
            return

        x_master, y_master = self.goal_master
        master_index_array = np.where((self.path == self.goal_master).all(axis=1))[0]

        if len(master_index_array) == 0:
            rospy.logwarn("Master index not found in path")
            return

        master_index = master_index_array[0]

        if self.forward_slave_goal:
            for i in range(master_index + 1, len(self.path)):
                x, y = self.path[i]
                distance = math.sqrt((x - x_master) ** 2 + (y - y_master) ** 2)
                if abs(distance - self.distance_master) < 0.01:
                    self.goal_slave = [x, y]
                    self.distance_flag_slave = True
                    self.publish_goal_marker(self.goal_slave, self.slave_goal_marker_pub, "slave_goal_marker", 1, (0.0, 0.0, 1.0))
                    break
        else:
            for i in range(master_index - 1, -1, -1):
                x, y = self.path[i]
                distance = math.sqrt((x - x_master) ** 2 + (y - y_master) ** 2)
                if abs(distance - self.distance_master) < 0.01:
                    self.goal_slave = [x, y]
                    self.distance_flag_slave = True
                    self.publish_goal_marker(self.goal_slave, self.slave_goal_marker_pub, "slave_goal_marker", 1, (0.0, 0.0, 1.0))
                    break

        if not self.distance_flag_slave:
            rospy.logwarn("No valid slave goal found within criteria")
            self.distance_flag_slave = False

    def odom_slave_callback(self, msg):
        # Check if node is active before proceeding
        if not self.node_active:
            return

        distance_x = self.slave_filter_x
        distance_y = self.slave_filter_y
        linear_x_in = msg.twist.twist.linear.x
        linear_y_in = msg.twist.twist.linear.y

        self.update_goal_slave()

        error_x_slave = self.goal_slave[0] - distance_x
        error_y_slave = self.goal_slave[1] - distance_y

        self.slave_error_x_pub.publish(Float64(error_x_slave))
        self.slave_error_y_pub.publish(Float64(error_y_slave))
        self.slave_input_linear_x_vel_pub.publish(Float64(linear_x_in))
        self.slave_input_linear_y_vel_pub.publish(Float64(linear_y_in))

    def vel_x_master_callback(self, msg):
        if not self.node_active:
            return
        self.master_linear_x_out = msg.data
        self.publish_velocity_master()

    def vel_y_master_callback(self, msg):
        if not self.node_active:
            return
        self.master_linear_y_out = msg.data
        self.publish_velocity_master()

    def vel_x_slave_callback(self, msg):
        if not self.node_active:
            return
        self.slave_linear_x_out = msg.data
        self.publish_velocity_slave()

    def vel_y_slave_callback(self, msg):
        if not self.node_active:
            return
        self.slave_linear_y_out = msg.data
        self.publish_velocity_slave()

    def publish_velocity_master(self):
        master_vel_out = Twist()
        master_vel_out.linear.x = getattr(self, 'master_linear_x_out', 0.0)
        master_vel_out.linear.y = getattr(self, 'master_linear_y_out', 0.0)
        self.master_vel_pub.publish(master_vel_out)

    def publish_velocity_slave(self):
        slave_vel_out = Twist()
        slave_vel_out.linear.x = getattr(self, 'slave_linear_x_out', 0.0)
        slave_vel_out.linear.y = getattr(self, 'slave_linear_y_out', 0.0)
        self.slave_vel_pub.publish(slave_vel_out)

    def publish_goal_marker(self, goal, publisher, ns, id, color):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.ns = ns
        marker.id = id
        marker.type = Marker.CYLINDER
        marker.action = Marker.ADD
        marker.pose.position.x = goal[0]
        marker.pose.position.y = goal[1]
        marker.pose.position.z = 0.0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.scale.z = 0.01
        marker.color.a = 1.0
        marker.color.r = color[0]
        marker.color.g = color[1]
        marker.color.b = color[2]
        publisher.publish(marker)

    def odom_master_filter(self, msg):
        self.master_filter_x = msg.pose.pose.position.x
        self.master_filter_y = msg.pose.pose.position.y

    def odom_slave_filter(self, msg):
        self.slave_filter_x = msg.pose.pose.position.x
        self.slave_filter_y = msg.pose.pose.position.y


if __name__ == '__main__':
    try:
        fuzzy_controller = CombinedPathStatusSubscriber()
        # Subscribers for master
        rospy.Subscriber('masterbot_kalman', Odometry, fuzzy_controller.odom_master_callback)
        rospy.Subscriber('output_linear_master_x_vel', Float64, fuzzy_controller.vel_x_master_callback)
        rospy.Subscriber('output_linear_master_y_vel', Float64, fuzzy_controller.vel_y_master_callback)
        rospy.Subscriber('master_filter', Odometry, fuzzy_controller.odom_master_filter)

        # Subscribers for slave
        rospy.Subscriber('slavebot_kalman', Odometry, fuzzy_controller.odom_slave_callback)
        rospy.Subscriber('output_linear_slave_x_vel', Float64, fuzzy_controller.vel_x_slave_callback)
        rospy.Subscriber('output_linear_slave_y_vel', Float64, fuzzy_controller.vel_y_slave_callback)
        rospy.Subscriber('slave_filter', Odometry, fuzzy_controller.odom_slave_filter)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
