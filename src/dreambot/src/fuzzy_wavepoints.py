#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Twist, PoseStamped
from visualization_msgs.msg import Marker
import numpy as np
import math

class TargetVelocityController:
    def __init__(self):
        self.distance_master = rospy.get_param('~distance_master', 1.5)

        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

        # Generate the path
        self.path = self.generate_path()

        self.reached_final_waypoint = False
        self.distance_flag = False
        self.distance_to_goal = 0.0
        master_pos = np.array([self.distance_master, 0])
        self.goal_master = [self.distance_master, 0.0]

        # Find the closest point in the path to master_pos
        distances = np.linalg.norm(self.path - master_pos, axis=1)
        self.count_master = np.argmin(distances)

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

    def generate_path(self):
        diameter1 = 3
        radius1 = diameter1 / 2

        diameter2 = 2
        radius2 = diameter2 / 2

        num_points = 10000

        theta1 = np.linspace(-np.pi/2, np.pi/2, num_points)
        theta2 = np.linspace(np.pi/2, np.pi, num_points)

        x1 = radius1 * np.cos(theta1)
        y1 = radius1 * np.sin(theta1)
        x2 = radius2 * np.cos(theta2)
        y2 = radius2 * np.sin(theta2)

        half_circle1 = np.column_stack((x1 + 2, y1 + 1.5))
        half_circle2 = np.column_stack((x2 + 1, y2 + 2))

        path1 = np.column_stack((np.linspace(0, 7, num_points), np.full(num_points, -1)))
        path2 = np.column_stack((np.linspace(7, 9.5, num_points), np.linspace(-1, 0, num_points) -0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path3 = np.column_stack((np.full(num_points, 9.5), np.linspace(0, 4, num_points)))
        path6 = np.column_stack((np.linspace(9.5, 8, num_points), np.linspace(4, 5.5, num_points)+ 0.5 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path7 = np.column_stack((np.linspace(8, 3, num_points), np.full(num_points, 5.5)))
        path8 = np.column_stack((np.linspace(3, 0, num_points), np.linspace(5.5, 2, num_points) + 0.8 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path9 = np.column_stack((np.linspace(0, -3, num_points), np.linspace(2, -1, num_points) - 0.8 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path10 = np.column_stack((np.linspace(-3, -7, num_points), np.full(num_points, -1)))
        path11 = np.column_stack((np.linspace(-7, -8.5, num_points), np.linspace(-1, 1, num_points)- 0.6 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path12 = np.column_stack((np.full(num_points, -8.5), np.linspace(1, 4, num_points)))
        path13 = np.column_stack((np.linspace(-8.5, -7, num_points), np.linspace(4, 5.5, num_points)+ 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path14 = np.column_stack((np.linspace(-7, 1, num_points),np.full(num_points, 5.5)))

        path4 = np.column_stack((np.zeros(num_points), np.linspace(0, -4, num_points)))
        a1 = 0.2
        f1 = 0.75 * np.pi
        path4[:, 0] += a1 * np.sin(f1 * path4[:, 1])

        path5 = np.column_stack((np.linspace(0, 4, num_points), np.full(num_points, -4)))
        a2 = 0.2
        f2 = 0.75 * -np.pi
        path5[:, 1] += a2 * np.sin(f2 * path5[:, 0])

        return np.vstack((path1, path2, path3, path6, path7, path8, path9, path10, path11, path12, path13, path14))

    def publish_path(self):
        path_points = self.generate_path()

        path_msg = Path()
        path_msg.header.stamp = rospy.Time.now()
        path_msg.header.frame_id = "map"

        for point in path_points:
            pose = PoseStamped()
            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "map"
            pose.pose.position.x = point[0]
            pose.pose.position.y = point[1]
            pose.pose.position.z = 0
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0
            path_msg.poses.append(pose)

        self.path_pub.publish(path_msg)

    def odom_master_callback(self, msg):
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
        x_master, y_master = self.goal_master
        min_distance = float('inf')
        best_index = None

        master_index_array = np.where((self.path == self.goal_master).all(axis=1))[0]
        if len(master_index_array) == 0:
            rospy.logwarn("Master index not found in path")
            return
        master_index = master_index_array[0]

        if master_index >= len(self.path):
            master_index = len(self.path) - 1

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
        self.master_linear_x_out = msg.data
        self.publish_velocity_master()

    def vel_y_master_callback(self, msg):
        self.master_linear_y_out = msg.data
        self.publish_velocity_master()

    def vel_x_slave_callback(self, msg):
        self.slave_linear_x_out = msg.data
        self.publish_velocity_slave()

    def vel_y_slave_callback(self, msg):
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
    rospy.init_node('combined_fuzzy_dreambot_node')

    fuzzy_controller = TargetVelocityController()

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

    # Publish the path
    while not rospy.is_shutdown():
        fuzzy_controller.publish_path()
        fuzzy_controller.rate.sleep()

    rospy.spin()
