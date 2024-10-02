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
import threading  

class CombinedPathStatusSubscriber:
    def __init__(self):
        rospy.init_node('leader_switch_combine', anonymous=True)

        self.distance_master = None
        self.forward_slave_goal = None
        self.path = None
        self.count_master = 0

        # Subscribers for status and activation
        self.status_sub = rospy.Subscriber('/combined_path_status', CombinedPathStatus, self.status_callback)
        self.activate_sub = rospy.Subscriber('/activate_base_station', BoolInt, self.activate_callback, queue_size=20)

        # Node states and goals
        self.node_active = False
        self.reached_final_waypoint = False
        self.distance_flag = False
        self.distance_to_goal = 0.0
        self.goal_master = [0.0, 0.0]
        self.stop_publishing = False  # New flag to stop publishing after goal is reached

        self.reached_final_waypoint_slave = False
        self.distance_flag_slave = False
        self.goal_slave = [0.0, 0.0]

        # Filter values
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
        self.slave_input_linear_y_vel_pub = rospy.Publisher('input_linear_y_vel', Float64, queue_size=1)
        self.slave_vel_pub = rospy.Publisher('slave_cmd_vel', Twist, queue_size=10)
        self.slave_goal_marker_pub = rospy.Publisher('slave_goal_marker', Marker, queue_size=10)

    def status_callback(self, msg):
        # Update forward_slave_goal and path from CombinedPathStatus message
        self.node_active = msg.node_active
        self.forward_slave_goal = msg.path_published
        self.path = self.format_combined_path(msg.path.x, msg.path.y)
        if self.path is not None and self.distance_master is not None:
            # Find the closest point in the path to master_pos
            master_pos = np.array([self.distance_master, 0])
            distances = np.linalg.norm(self.path - master_pos, axis=1)
            self.count_master = np.argmin(distances)

        # Reset stop_publishing if node becomes active again
        if self.node_active and self.stop_publishing:
            self.stop_publishing = False
            self.reached_final_waypoint = False

    def format_combined_path(self, x_coords, y_coords):
        if not x_coords or not y_coords:
            rospy.logwarn("Received empty path coordinates.")
            return None
        x_array = np.array(x_coords)
        y_array = np.array(y_coords)
        return np.column_stack((x_array, y_array))

    def activate_callback(self, msg):
        # Set distance_master from the activation message
        self.distance_master = msg.number

    def odom_master_callback(self, msg):
        # Stop all publishing activities if goal is reached
        if self.stop_publishing:
            return

        # Check if node is active and both distance_master and path are initialized before proceeding
        if not self.node_active or self.path is None or self.distance_master is None:
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
        # Calculate the current position of the master
        current_position = np.array([distance_x, distance_y])

        # Stop updating master goal if the slave has reached the end of the path
        if self.reached_final_waypoint:
            rospy.loginfo("Master goal updates stopped because slave reached the end of the path.")
            threading.Thread(target=self.stop_with_delay).start()  # Start a thread to handle delay and stopping
            return

        # Find the closest point in the path to the master
        if self.path is None:
            return

        distances = np.linalg.norm(self.path - current_position, axis=1)
        closest_index = np.argmin(distances)

        # Check if the closest point is at the end of the path
        if closest_index >= len(self.path) - 1:
            rospy.loginfo("Master has reached the end of the path.")
            self.reached_final_waypoint = True
            self.goal_master = self.path[-1]
            threading.Thread(target=self.stop_with_delay).start()  # Start a thread to handle delay and stopping
            return

        # Look for the next goal point that is 0.1 units ahead of the master
        for i in range(closest_index, len(self.path)):
            point = self.path[i]
            distance_to_point = np.linalg.norm(point - current_position)

            # If the point is at least 0.1 units away, set it as the next goal
            if distance_to_point >= 0.1:
                self.goal_master = point
                self.distance_flag = True
                self.publish_goal_marker(self.goal_master, self.master_goal_marker_pub, "master_goal_marker", 0, (1.0, 0.0, 0.0))
                break

        # Reset the flag if the goal is reached
        if self.distance_to_goal < 0.1:
            self.distance_flag = False

    def publish_zero_velocity(self):
        """Publish zero velocities to both master and slave and stop further publishing."""
        zero_twist = Twist()
        zero_twist.linear.x = 0.0
        zero_twist.linear.y = 0.0
        self.master_vel_pub.publish(zero_twist)
        self.slave_vel_pub.publish(zero_twist)
        rospy.loginfo("Published zero velocities to both master and slave.")

    def stop_with_delay(self):
        """Delay publishing zero velocities to allow for a brief pause after reaching the goal."""
        rospy.sleep(3) 
        self.publish_zero_velocity()
        self.stop_publishing = True  

    def update_goal_slave(self):
        # Stop all publishing activities if goal is reached
        if self.stop_publishing:
            return

        x_master, y_master = self.goal_master

        master_index_array = np.where((self.path == self.goal_master).all(axis=1))[0]
        if len(master_index_array) == 0:
            rospy.logwarn("Master index not found in path")
            return
        master_index = master_index_array[0]

        if self.forward_slave_goal:
            # Look forward in the path for the slave goal
            for i in range(master_index + 1, len(self.path)):
                x, y = self.path[i]
                distance = math.sqrt((x - x_master) ** 2 + (y - y_master) ** 2)
                if abs(distance - self.distance_master) < 0.01:
                    self.goal_slave = [x, y]
                    self.distance_flag_slave = True
                    self.publish_goal_marker(self.goal_slave, self.slave_goal_marker_pub, "slave_goal_marker", 1, (0.0, 0.0, 1.0))
                    
                    # Check if the slave goal is within a small tolerance from the last point in the path
                    if np.linalg.norm(np.array(self.goal_slave) - np.array(self.path[-1])) < 0.05:
                        rospy.loginfo("Slave has reached the end of the path.")
                        self.reached_final_waypoint = True  # Mark master goal as reached
                        threading.Thread(target=self.stop_with_delay).start()  # Start a thread to handle delay and stopping
                    break
        else:
            # Look backward in the path for the slave goal (existing behavior)
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
        # Stop all publishing activities if goal is reached
        if self.stop_publishing:
            return

        # Check if node is active, distance_master, and path are initialized
        if not self.node_active or self.path is None or self.distance_master is None:
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
        if not self.node_active or self.stop_publishing:
            return
        self.master_linear_x_out = msg.data
        self.publish_velocity_master()

    def vel_y_master_callback(self, msg):
        if not self.node_active or self.stop_publishing:
            return
        self.master_linear_y_out = msg.data
        self.publish_velocity_master()

    def vel_x_slave_callback(self, msg):
        if not self.node_active or self.stop_publishing:
            return
        self.slave_linear_x_out = msg.data
        self.publish_velocity_slave()

    def vel_y_slave_callback(self, msg):
        if not self.node_active or self.stop_publishing:
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
        if self.stop_publishing:
            return
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
