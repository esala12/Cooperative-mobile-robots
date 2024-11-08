#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
import csv
import os

class MasterFilterDataCollector:
    def __init__(self):
        # Set the path for the CSV file
        self.csv_file_path = os.path.expanduser('~/data/master_filter_data.csv')
        
        # Create the CSV file and write the header
        with open(self.csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = [
                'timestamp', 'position_x', 'position_y', 'position_z',
                'orientation_x', 'orientation_y', 'orientation_z', 'orientation_w',
                'linear_velocity_x', 'linear_velocity_y', 'linear_velocity_z',
                'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z'
            ]
            self.writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            self.writer.writeheader()
        
        # Initialize subscriber
        self.subscriber = rospy.Subscriber('/master_filter', Odometry, self.odometry_callback)
        rospy.loginfo("Subscriber initialized. Writing data to %s", self.csv_file_path)
        
    def odometry_callback(self, msg):
        # Get the current time
        timestamp = rospy.get_time()
        
        # Append new data to the CSV file
        with open(self.csv_file_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                timestamp,
                msg.pose.pose.position.x,
                msg.pose.pose.position.y,
                msg.pose.pose.position.z,
                msg.pose.pose.orientation.x,
                msg.pose.pose.orientation.y,
                msg.pose.pose.orientation.z,
                msg.pose.pose.orientation.w,
                msg.twist.twist.linear.x,
                msg.twist.twist.linear.y,
                msg.twist.twist.linear.z,
                msg.twist.twist.angular.x,
                msg.twist.twist.angular.y,
                msg.twist.twist.angular.z
            ])
        rospy.loginfo("Data recorded at timestamp %f", timestamp)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('master_filter_data_collector')
    collector = MasterFilterDataCollector()
    rospy.spin()
