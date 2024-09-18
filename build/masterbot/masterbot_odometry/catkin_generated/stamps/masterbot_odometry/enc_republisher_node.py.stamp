#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry  

def odomCallback(msg):
    msg.header.frame_id = "master_odom_ekf"
    msg.child_frame_id = "master_base_footprint_ekf"
    odom_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('odom_republisher_node')
    odom_pub = rospy.Publisher('master_odom_ekf', Odometry, queue_size=10) 
    odom_sub = rospy.Subscriber('master_odom', Odometry, odomCallback)      

    rospy.spin()
