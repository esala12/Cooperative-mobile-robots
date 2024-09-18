#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

import numpy as np
import matplotlib.pyplot as plt
import math

class TargetVelocityController:
    def __init__(self):
        self.A = [2.0, -2.0]
        self.B = [2.0, 0.0]
        self.C = [2.0, 2.0]
        self.D = [0.0, 0.0]
        self.E = [-2.0,-2.0]
        self.F = [-2.0, 0.0]
        self.G = [0.0, 0.0]
        self.wavepoints = [self.A, self.B, self.C, self.D, self.E, self.F, self.G]
        self.count = 0
        self.reached_final_waypoint = False

        self.linear_x_in = 0.0
        self.distance_x = 0.0
        self.linear_x_out = 0.0  
        self.error_x = self.wavepoints[self.count][0] - self.distance_x
        
        self.linear_y_in = 0.0
        self.distance_y = 0.0
        self.linear_y_out = 0.0
        self.error_y = self.wavepoints[self.count][1] - self.distance_y

        # Error x direction
        self.error_x_pub = rospy.Publisher('error_x', Float64, queue_size=1)
        self.input_linear_vel_pub = rospy.Publisher('input_linear_vel', Float64, queue_size=1)

        # Error y direction
        self.error_y_pub = rospy.Publisher('error_y', Float64, queue_size=1)
        self.input_linear_y_vel_pub = rospy.Publisher('input_linear_y_vel', Float64, queue_size=1)

        self.vel_pub = rospy.Publisher('master_cmd_vel', Twist, queue_size=10)

    def odom_callback(self, msg):
        # Error x direction
        self.linear_x_in = msg.twist.twist.linear.x
        self.distance_x = msg.pose.pose.position.x
        self.error_x = self.wavepoints[self.count][0] - self.distance_x
        self.error_x_pub.publish(Float64(self.error_x))
        
        # Error y direction
        self.linear_y_in = msg.twist.twist.linear.y
        self.distance_y = msg.pose.pose.position.y
        self.error_y = self.wavepoints[self.count][1] - self.distance_y
        self.error_y_pub.publish(Float64(self.error_y))

        # Input linear x velocity
        self.input_linear_vel_pub.publish(Float64(self.linear_x_in))

        # Input linear y velocity
        self.input_linear_y_vel_pub.publish(Float64(self.linear_y_in))

        distance_to_waypoint = math.sqrt(self.error_x**2 + self.error_y**2)
        
        if distance_to_waypoint < 0.1:
            self.count += 1
            if self.count >= len(self.wavepoints):
                self.count = len(self.wavepoints) - 1
                self.reached_final_waypoint = True

    def vel_x_callback(self, msg):
        self.linear_x_out = msg.data

        vel_out = Twist()
        if not self.reached_final_waypoint:
            vel_out.linear.x = self.linear_x_out
            vel_out.linear.y = self.linear_y_out
        self.vel_pub.publish(vel_out)

    def vel_y_callback(self, msg):
        self.linear_y_out = msg.data

        vel_out = Twist()
        if not self.reached_final_waypoint:
            vel_out.linear.x = self.linear_x_out
            vel_out.linear.y = self.linear_y_out
        self.vel_pub.publish(vel_out)

if __name__ == '__main__':
    rospy.init_node('fuzzy_matlab_node')

    fuzzy_controller = TargetVelocityController()

    rospy.Subscriber('master_odom', Odometry, fuzzy_controller.odom_callback)
    rospy.Subscriber('output_linear_vel', Float64, fuzzy_controller.vel_x_callback)
    rospy.Subscriber('output_linear_y_vel', Float64, fuzzy_controller.vel_y_callback)

    rospy.spin()
