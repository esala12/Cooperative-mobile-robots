#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

def imuCallback(imu):
     imu.header.frame_id = "base_footprint_ekf"
     imu_pub.publish(imu)


if __name__ == '__main__':
     rospy.init_node('imu_republisher_node')
     imu_pub = rospy.Publisher('master_imu_ekf', Imu, queue_size=10)
     imu_sub = rospy.Subscriber('masterbot_imu', Imu, imuCallback)

     
     rospy.spin()
