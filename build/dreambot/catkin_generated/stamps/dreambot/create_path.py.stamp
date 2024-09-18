#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import numpy as np

class PathGeneratorNode:
    def __init__(self):
        self.path_pub = rospy.Publisher('/generated_path', Path, queue_size=10)
        self.rate = rospy.Rate(1)  # 1 Hz publishing rate

    def generate_path(self):
        # Path generation logic from the original code
        diameter1 = 3
        radius1 = diameter1 / 2
        diameter2 = 2
        radius2 = diameter2 / 2
        num_points = 10000

        theta1 = np.linspace(-np.pi / 2, np.pi / 2, num_points)
        theta2 = np.linspace(np.pi / 2, np.pi, num_points)
        x1 = radius1 * np.cos(theta1)
        y1 = radius1 * np.sin(theta1)
        x2 = radius2 * np.cos(theta2)
        y2 = radius2 * np.sin(theta2)

        # Define paths as in the original code
        path1 = np.column_stack((np.linspace(0, 7, num_points), np.full(num_points, -1)))

        return np.vstack((path1))

    def publish_path(self):
        path_points = self.generate_path()

        path_msg = Path()
        path_msg.header.stamp = rospy.Time.now()
        path_msg.header.frame_id = "map"

        for point in path_points:
            pose = PoseStamped()
            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "map"
            pose.pose.position.x = point[0]
            pose.pose.position.y = point[1]
            pose.pose.position.z = 0
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0
            path_msg.poses.append(pose)

        self.path_pub.publish(path_msg)

    def run(self):
        while not rospy.is_shutdown():
            self.publish_path()
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('path_generator_node')
    path_generator = PathGeneratorNode()
    path_generator.run()
