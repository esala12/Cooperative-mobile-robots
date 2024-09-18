#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

import numpy as np
import math

class TargetVelocityController:
    def __init__(self):

        points1 = np.column_stack((np.linspace(0, 3, 1000), np.zeros(1000)))
        points2 = np.column_stack((np.full(1000, 3), np.linspace(0, 3, 1000)))
        points3 = np.column_stack((np.linspace(3,0,1000), np.full(1000, 3)))
        points4 = np.column_stack((np.zeros(1000), np.linspace(3,0,1000)))
        amplitude = 0.5   
        frequency = 1.0 * np.pi
        points1[:, 1] += amplitude * np.sin(frequency * points1[:, 0])
        points2[:, 0] += amplitude * np.sin(frequency * points2[:, 1])
        points3[:, 1] += amplitude * np.sin(frequency * points3[:, 0])
        points4[:, 0] += amplitude * np.sin(frequency * points4[:, 1])
        
        self.path = np.vstack((points1, points2, points3, points4))
        
        self.count = 0
        self.reached_final_waypoint = False
        self.distance_flag = False
        self.distance_to_goal = 0.0
        self.goal = [0.0, 0.0]

        # Publishers
        self.error_x_pub = rospy.Publisher('error_x', Float64, queue_size=1)
        self.input_linear_vel_pub = rospy.Publisher('input_linear_vel', Float64, queue_size=1)
        self.error_y_pub = rospy.Publisher('error_y', Float64, queue_size=1)
        self.input_linear_y_vel_pub = rospy.Publisher('input_linear_y_vel', Float64, queue_size=1)
        self.vel_pub = rospy.Publisher('master_cmd_vel', Twist, queue_size=10)

    def odom_callback(self, msg):
        # Extract positions and velocities from Odometry message
        distance_x = msg.pose.pose.position.x
        distance_y = msg.pose.pose.position.y
        linear_x_in = msg.twist.twist.linear.x
        linear_y_in = msg.twist.twist.linear.y

        # Update the goal
        self.update_goal(distance_x, distance_y)

        # Compute errors
        error_x = self.goal[0] - distance_x
        error_y = self.goal[1] - distance_y
        self.distance_to_goal = math.sqrt(error_x**2 + error_y**2)

        # Publish errors and input velocities
        self.error_x_pub.publish(Float64(error_x))
        self.error_y_pub.publish(Float64(error_y))
        self.input_linear_vel_pub.publish(Float64(linear_x_in))
        self.input_linear_y_vel_pub.publish(Float64(linear_y_in))

    def update_goal(self, distance_x, distance_y):
        while not self.reached_final_waypoint and not self.distance_flag:
            if self.count >= len(self.path):
                self.reached_final_waypoint = True
                self.goal = self.path[-1]
                break

            x_val, y_val = self.path[self.count]
            distance_to_point = math.sqrt((x_val - distance_x)**2 + (y_val - distance_y)**2)

            if distance_to_point >= 0.1:
                self.goal = [x_val, y_val]
                self.distance_flag = True
            else:
                self.count += 1

        if self.distance_to_goal < 0.1:
            self.distance_flag = False

    def vel_x_callback(self, msg):
        self.linear_x_out = msg.data
        self.publish_velocity()

    def vel_y_callback(self, msg):
        self.linear_y_out = msg.data
        self.publish_velocity()

    def publish_velocity(self):
        vel_out = Twist()
        vel_out.linear.x = getattr(self, 'linear_x_out', 0.0)
        vel_out.linear.y = getattr(self, 'linear_y_out', 0.0)
        self.vel_pub.publish(vel_out)

if __name__ == '__main__':
    rospy.init_node('fuzzy_matlab_node')

    fuzzy_controller = TargetVelocityController()

    rospy.Subscriber('masterbot_kalman', Odometry, fuzzy_controller.odom_callback)
    rospy.Subscriber('output_linear_vel', Float64, fuzzy_controller.vel_x_callback)
    rospy.Subscriber('output_linear_y_vel', Float64, fuzzy_controller.vel_y_callback)

    rospy.spin()
