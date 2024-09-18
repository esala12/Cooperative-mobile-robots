#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64

class TargetVelocityController:
     def __init__(self):
          self.target_linear_x = 0.0
          self.target_linear_y = 0.0
          self.target_angular_z = 0.0

     def cmd_vel_callback(self, msg):
          self.target_linear_x = msg.linear.x
          self.target_linear_y = msg.linear.y
          self.target_angular_z = msg.angular.z

     def odom_callback(self, msg):
          current_linear_x = msg.twist.twist.linear.x
          current_linear_y = msg.twist.twist.linear.y
          current_angular_z = msg.twist.twist.angular.z

          current_lvel.publish(current_linear_x)
          target_v.publish(self.target_linear_x)

     def tunedv_callback(self, msg):
          tunedv = msg.data
          twist_msg = Twist()
          twist_msg.linear.x = tunedv
          twist_pub.publish(twist_msg)

if __name__ == '__main__':
    rospy.init_node('masterbotpid', anonymous=True)
    
    target_controller = TargetVelocityController()
    
    rospy.Subscriber('/master_cmd_vel', Twist, target_controller.cmd_vel_callback) 
    rospy.Subscriber("/master_odom", Odometry, target_controller.odom_callback)
    rospy.Subscriber("/tuned_v", Float64, target_controller.tunedv_callback)

    twist_pub = rospy.Publisher('master_pid_vel', Twist, queue_size=10)
    current_lvel = rospy.Publisher('current_lvel', Float64, queue_size=1)
    target_v = rospy.Publisher('target_v', Float64, queue_size=1)

    rospy.spin()
