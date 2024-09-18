#!/usr/bin/env python3
import rospy
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped


class TfMasterbot(object):

    def __init__(self):
        self.static_broadcaster = StaticTransformBroadcaster()

        # LiDAR transform
        self.static_transform_lidar = TransformStamped()
        self.static_transform_lidar.header.frame_id = "master_base_footprint"
        self.static_transform_lidar.child_frame_id = "sick_lidar0"
        self.static_transform_lidar.transform.translation.x = 0.33
        self.static_transform_lidar.transform.translation.y = 0.0
        self.static_transform_lidar.transform.translation.z = 0.195722
        self.static_transform_lidar.transform.rotation.x = 0
        self.static_transform_lidar.transform.rotation.y = 0
        self.static_transform_lidar.transform.rotation.z = 0
        self.static_transform_lidar.transform.rotation.w = 1

        # IMU transform
        self.static_transform_imu = TransformStamped()
        self.static_transform_imu.header.frame_id = "master_base_footprint"
        self.static_transform_imu.child_frame_id = "IMU_sensor"
        self.static_transform_imu.transform.translation.x = 0.0
        self.static_transform_imu.transform.translation.y = 0.0
        self.static_transform_imu.transform.translation.z = 0.08
        self.static_transform_imu.transform.rotation.x = 0
        self.static_transform_imu.transform.rotation.y = 0
        self.static_transform_imu.transform.rotation.z = 0
        self.static_transform_imu.transform.rotation.w = 1

        # Publish transforms
        self.static_broadcaster.sendTransform([self.static_transform_lidar, self.static_transform_imu])

if __name__ == '__main__':
    rospy.init_node('tf_masterbot')
    tf_masterbot = TfMasterbot()
    rospy.spin()
