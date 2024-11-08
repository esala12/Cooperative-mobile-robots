#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import csv
import os

class CmdVelCollector:
    def __init__(self):
        # Set the path for the CSV file
        self.csv_file_path = os.path.expanduser('~/data/cmd_vel_data.csv')
        
        # Create the CSV file and write the header
        with open(self.csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ['timestamp', 'linear_x', 'linear_y', 'linear_z', 'angular_x', 'angular_y', 'angular_z']
            self.writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            self.writer.writeheader()
        
        # Initialize subscriber
        self.subscriber = rospy.Subscriber('/turtle1/cmd_vel', Twist, self.callback)
        rospy.loginfo("Subscriber initialized. Writing data to %s", self.csv_file_path)
        
    def callback(self, msg):
        # Get the current time
        timestamp = rospy.get_time()
        
        # Append new data to the CSV file
        with open(self.csv_file_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                timestamp,
                msg.linear.x,
                msg.linear.y,
                msg.linear.z,
                msg.angular.x,
                msg.angular.y,
                msg.angular.z
            ])
        rospy.loginfo("Data recorded at timestamp %f", timestamp)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('cmd_vel_to_csv')
    collector = CmdVelCollector()
    rospy.spin()
