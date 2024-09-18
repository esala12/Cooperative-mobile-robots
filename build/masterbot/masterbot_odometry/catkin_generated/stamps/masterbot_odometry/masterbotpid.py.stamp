#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32

# Global variables to store target linear and angular velocities
target_linear_x = 0.0
target_linear_y = 0.0
target_angular_z = 0.0

u_linear_x = 0.0
prop_x = 0.15
inte_x = 0.05
integral_error_linear_x = 0.0

u_linear_y = 0.0
prop_y = 0.15
inte_y = 0.05
integral_error_linear_y = 0.0

u_linear_theta = 0.0
prop_theta = 0.15
inte_theta = 0.05
integral_error_linear_theta = 0.0

def cmd_vel_callback(msg):
    global target_linear_x, target_linear_y, target_angular_z
    target_linear_x = msg.linear.x
    target_linear_y = msg.linear.y
    target_angular_z = msg.angular.z

def odom_callback(msg):
    global target_linear_x, target_linear_y, target_angular_z
    global prop_x, inte_x, u_linear_x,prop_y, inte_y, u_linear_y, prop_theta, inte_theta, u_linear_theta
    global integral_error_linear_x, integral_error_linear_y, integral_error_linear_theta

    current_linear_x = msg.twist.twist.linear.x
    current_linear_y = msg.twist.twist.linear.y
    current_angular_z = msg.twist.twist.angular.z

    error_linear_x = target_linear_x - current_linear_x
    error_linear_y = target_linear_y - current_linear_y
    error_angular_z = target_angular_z - current_angular_z

    # Integral term for linear x
    integral_error_linear_x += error_linear_x
    integral_x = inte_x * integral_error_linear_x

    # Control action for linear x
    u_linear_x = (prop_x * error_linear_x) + integral_x 

    # Limit u_linear_x to avoid large oscillations
    u_linear_x = max(min(u_linear_x, 1.0), -1.0)

    #Integral term for linear y
    integral_error_linear_y += error_linear_y
    integral_y = inte_y * integral_error_linear_y

    # Control action for linear y
    u_linear_y = (prop_y * error_linear_y) + integral_y

    # Limit u_linear_x to avoid large oscillations
    u_linear_y = max(min(u_linear_y, 1.0), -1.0)

    #Integral term for angular theta
    integral_error_linear_theta += error_angular_z
    integral_theta = inte_theta * integral_error_linear_theta

    # Control action for angular theta
    u_linear_theta = (prop_theta * error_angular_z) + integral_theta

    # Limit u_linear_x to avoid large oscillations
    u_linear_theta = max(min(u_linear_theta, 1.0), -1.0)
    
    twist_msg = Twist()
    twist_msg.linear.x = u_linear_x
    twist_msg.linear.y = u_linear_y
    twist_msg.angular.z = u_linear_theta

    twist_pub.publish(twist_msg)
    current_lvel.publish(u_linear_x)
    target_v.publish(target_linear_x)

def propCallback(msg):
    global prop_x
    prop_x = msg.data

def inteCallback(msg):
    global inte_x
    inte_x = msg.data

if __name__ == '__main__':
    rospy.init_node('masterbotpid', anonymous=True)    
    rospy.Subscriber('/master_cmd_vel', Twist, cmd_vel_callback) 
    rospy.Subscriber("/master_odom", Odometry, odom_callback)
    rospy.Subscriber('/prop', Float32, propCallback)
    rospy.Subscriber('/inte', Float32, inteCallback)

    twist_pub = rospy.Publisher('master_pid_vel', Twist, queue_size=10)
    current_lvel = rospy.Publisher('current_lvel', Float32, queue_size=1)
    target_v = rospy.Publisher('target_v', Float32, queue_size=1)

    rospy.spin()
