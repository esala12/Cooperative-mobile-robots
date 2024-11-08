#!/usr/bin/env python3
import rospy
from tf2_ros import StaticTransformBroadcaster, TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry

class TfMasterbot(object):

    def __init__(self):
        # Subscriber for the odometry topic
        self.odom_sub_ = rospy.Subscriber("/masterbot_kalman", Odometry, self.imuCallback)
        
        # Static transform broadcaster
        self.static_broadcaster = StaticTransformBroadcaster()
        
        # Dynamic transform broadcaster
        self.dynamic_broadcaster = TransformBroadcaster()

        # Map transform
        self.static_transform_map = TransformStamped()
        self.static_transform_map.header.frame_id = "map"
        self.static_transform_map.child_frame_id = "master_odom"
        self.static_transform_map.transform.translation.x = 0.0
        self.static_transform_map.transform.translation.y = 0.0
        self.static_transform_map.transform.translation.z = 0.0
        self.static_transform_map.transform.rotation.x = 0
        self.static_transform_map.transform.rotation.y = 0
        self.static_transform_map.transform.rotation.z = 0
        self.static_transform_map.transform.rotation.w = 1

        # LiDAR transform
        self.static_transform_lidar = TransformStamped()
        self.static_transform_lidar.header.frame_id = "master_base_footprint_ekf"
        self.static_transform_lidar.child_frame_id = "master_lidar"
        self.static_transform_lidar.transform.translation.x = 0.0
        self.static_transform_lidar.transform.translation.y = 0.0
        self.static_transform_lidar.transform.translation.z = 0.195722
        self.static_transform_lidar.transform.rotation.x = 0
        self.static_transform_lidar.transform.rotation.y = 0
        self.static_transform_lidar.transform.rotation.z = 0
        self.static_transform_lidar.transform.rotation.w = 1

        # IMU transform
        self.static_transform_imu = TransformStamped()
        self.static_transform_imu.header.frame_id = "master_base_footprint_ekf"
        self.static_transform_imu.child_frame_id = "IMU_sensor"
        self.static_transform_imu.transform.translation.x = 0.0
        self.static_transform_imu.transform.translation.y = 0.0
        self.static_transform_imu.transform.translation.z = 0.08
        self.static_transform_imu.transform.rotation.x = 0
        self.static_transform_imu.transform.rotation.y = 0
        self.static_transform_imu.transform.rotation.z = 0
        self.static_transform_imu.transform.rotation.w = 1

        # Publish static transforms
        self.static_broadcaster.sendTransform([self.static_transform_map, self.static_transform_lidar, self.static_transform_imu])

    def imuCallback(self, msg):
        # Create a TransformStamped message from the Odometry message
        dynamic_transform = TransformStamped()
        dynamic_transform.header.stamp = rospy.Time.now()
        dynamic_transform.header.frame_id = "master_odom"
        dynamic_transform.child_frame_id = "master_base_footprint_ekf"
        dynamic_transform.transform.translation.x = msg.pose.pose.position.x
        dynamic_transform.transform.translation.y = msg.pose.pose.position.y
        dynamic_transform.transform.translation.z = msg.pose.pose.position.z
        dynamic_transform.transform.rotation = msg.pose.pose.orientation

        # Publish the dynamic transform
        self.dynamic_broadcaster.sendTransform(dynamic_transform)

if __name__ == '__main__':
    rospy.init_node('tf_kalman_node')
    tf_masterbot = TfMasterbot()
    rospy.spin()
