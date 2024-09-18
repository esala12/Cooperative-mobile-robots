#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class TargetVelocityController:
    def __init__(self):
        self.error_x = 0.0
        self.linear_x_in = 0.0
        self.distance_x = 0.0
        self.target_x = 2.0
        self.linear_x_out = 0.0

        self.error_y = 0.0
        self.linear_y_in = 0.0
        self.distance_y = 0.0
        self.target_y = -2.0
        self.linear_y_out = 0.0

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
        self.error_x = self.target_x - self.distance_x
        self.error_x_pub.publish(Float64(self.error_x))
        
        # Error y direction
        self.linear_y_in = msg.twist.twist.linear.y
        self.distance_y = msg.pose.pose.position.y
        self.error_y = self.target_y - self.distance_y
        self.error_y_pub.publish(Float64(self.error_y))

        # Input linear x velocity
        self.input_linear_vel_pub.publish(Float64(self.linear_x_in))

        # Input linear y velocity
        self.input_linear_y_vel_pub.publish(Float64(self.linear_y_in))

    def vel_x_callback(self, msg):
        self.linear_x_out = msg.data

        vel_out = Twist()
        vel_out.linear.x = self.linear_x_out
        vel_out.linear.y = self.linear_y_out
        self.vel_pub.publish(vel_out)

    def vel_y_callback(self, msg):
        self.linear_y_out = msg.data

        vel_out = Twist()
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
