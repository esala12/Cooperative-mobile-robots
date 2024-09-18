#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
import numpy as np

class PathPublisher:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('path_publisher', anonymous=True)
        
        # Create a publisher for the Path message
        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)
        
        # Set the publishing rate
        self.rate = rospy.Rate(10) # 10 Hz

    def generate_path(self):
        # Generate path points
          amplitude = 0.5
          frequency = 1.0 * np.pi
          points1 = np.column_stack((np.linspace(0, 3, 1000), np.zeros(1000)))
          points2 = np.column_stack((np.full(1000, 3), np.linspace(0, 3, 1000)))
          points3 = np.column_stack((np.linspace(3,0,1000), np.full(1000, 3)))
          points4 = np.column_stack((np.zeros(1000), np.linspace(3,0,1000)))
          points1[:, 1] += amplitude * np.sin(frequency * points1[:, 0])
          points2[:, 0] += amplitude * np.sin(frequency * points2[:, 1])
          points3[:, 1] += amplitude * np.sin(frequency * points3[:, 0])
          points4[:, 0] += amplitude * np.sin(frequency * points4[:, 1])

          path_points = np.vstack((points1, points2, points3, points4))

          return path_points

    def publish_path(self):
        while not rospy.is_shutdown():
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
            self.rate.sleep()

if __name__ == '__main__':
    try:
        path_publisher = PathPublisher()
        path_publisher.publish_path()
    except rospy.ROSInterruptException:
        pass
