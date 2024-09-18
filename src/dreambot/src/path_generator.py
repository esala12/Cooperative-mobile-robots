#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path, Odometry
from std_msgs.msg import Float64
import math

class PathPublisher:
    def __init__(self):
        self.path_pub = rospy.Publisher('/path_diff', Path, queue_size=10)
        self.payload_dis_pub = rospy.Publisher('/payload_dis_pub', Float64, queue_size=10)
        self.master_pos = None
        self.slave_pos = None

        # Initialize the Path message
        self.path_msg = Path()
        self.path_msg.header.frame_id = "map"  # Adjust this frame ID as necessary

    def odom_master_callback(self, msg):
        distance_x = msg.pose.pose.position.x
        distance_y = msg.pose.pose.position.y
        self.master_pos = [distance_x, distance_y]
        self.publish_path()

    def odom_slave_callback(self, msg):
        distance_x = msg.pose.pose.position.x
        distance_y = msg.pose.pose.position.y
        self.slave_pos = [distance_x, distance_y]
        self.publish_path()

    def publish_path(self):
        if self.master_pos is not None and self.slave_pos is not None:
            # Calculate the distance
            payload_dis = math.sqrt(((self.master_pos[0] - self.slave_pos[0])**2) + ((self.master_pos[1] - self.slave_pos[1])**2))

            # Publish the payload distance
            payload_dis_msg = Float64()
            payload_dis_msg.data = payload_dis
            self.payload_dis_pub.publish(payload_dis_msg)

            # Create PoseStamped for slave position
            slave_pose = PoseStamped()
            slave_pose.header.stamp = rospy.Time.now()
            slave_pose.header.frame_id = self.path_msg.header.frame_id
            slave_pose.pose.position.x = self.slave_pos[0]
            slave_pose.pose.position.y = self.slave_pos[1]
            slave_pose.pose.orientation.w = 1.0  # Assuming no orientation data

            # Create PoseStamped for master position
            master_pose = PoseStamped()
            master_pose.header.stamp = rospy.Time.now()
            master_pose.header.frame_id = self.path_msg.header.frame_id
            master_pose.pose.position.x = self.master_pos[0]
            master_pose.pose.position.y = self.master_pos[1]
            master_pose.pose.orientation.w = 1.0  # Assuming no orientation data

            # Add the poses to the path (assuming we want to visualize the latest positions)
            self.path_msg.poses = [slave_pose, master_pose]

            # Publish the path
            self.path_msg.header.stamp = rospy.Time.now()
            self.path_pub.publish(self.path_msg)

if __name__ == '__main__':
    rospy.init_node('path_publisher', anonymous=True)
    path_publisher = PathPublisher()
    rospy.Subscriber('master_filter', Odometry, path_publisher.odom_master_callback)
    rospy.Subscriber('slave_filter', Odometry, path_publisher.odom_slave_callback)
    rospy.spin()
