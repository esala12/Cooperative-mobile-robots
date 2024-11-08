#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import csv
import os

class PayloadDataCollector:
    def __init__(self):
        # Set the path for the CSV file
        self.csv_file_path = os.path.expanduser('~/data/payload_data.csv')
        
        # Create the CSV file and write the header
        with open(self.csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ['timestamp', 'payload_distance']
            self.writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            self.writer.writeheader()
        
        # Initialize subscriber
        self.subscriber_payload = rospy.Subscriber('/payload_dis_pub', Float64, self.payload_callback)
        rospy.loginfo("Subscriber initialized. Writing data to %s", self.csv_file_path)
        
    def payload_callback(self, msg):
        # Get the current time
        timestamp = rospy.get_time()
        
        # Append new data to the CSV file
        with open(self.csv_file_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                timestamp,
                msg.data
            ])
        rospy.loginfo("Data recorded at timestamp %f with payload distance %f", timestamp, msg.data)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('payload_data_collector')
    collector = PayloadDataCollector()
    rospy.spin()
