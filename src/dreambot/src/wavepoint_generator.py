#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import numpy as np

class PathGenerator:
    def __init__(self):
        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

    def generate_path(self):
        diameter1 = 3
        radius1 = diameter1 / 2

        diameter2 = 2
        radius2 = diameter2 / 2

        num_points = 10000

        theta1 = np.linspace(-np.pi/2, np.pi/2, num_points)
        theta2 = np.linspace(np.pi/2, np.pi, num_points)

        x1 = radius1 * np.cos(theta1)
        y1 = radius1 * np.sin(theta1)
        x2 = radius2 * np.cos(theta2)
        y2 = radius2 * np.sin(theta2)

        half_circle1 = np.column_stack((x1 + 2, y1 + 1.5))
        half_circle2 = np.column_stack((x2+1, y2 + 2))

        path1 = np.column_stack((np.linspace(0, 2, num_points), np.zeros(num_points)))
        path2 = np.column_stack((np.linspace(2, 1, 10000), np.full(10000, 3)))
        path3 = np.column_stack((np.zeros(num_points), np.linspace(2, 0, num_points)))

        path4 = np.column_stack((np.zeros(num_points), np.linspace(0, -4, num_points)))
        a1 = 0.2 
        f1 = 0.75 * np.pi
        path4[:, 0] += a1 * np.sin(f1 * path4[:, 1])

        path5 = np.column_stack((np.linspace(0, 4, num_points), np.full(num_points, -4)))
        a2 = 0.2 
        f2 = 0.75 * -np.pi
        path5[:, 1] += a2 * np.sin(f2 * path5[:, 0])

        return np.vstack((path1, half_circle1, path2, half_circle2, path3, path4, path5))

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

if __name__ == '__main__':
    rospy.init_node('path_generator_node')

    path_generator = PathGenerator()

    while not rospy.is_shutdown():
        path_generator.publish_path()
        path_generator.rate.sleep()

    rospy.spin()
