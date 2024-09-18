#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class PathSelectorNode:
    def __init__(self):
        rospy.init_node('path_selector_node')
        self.path_pub = rospy.Publisher('/selected_path', String, queue_size=10)
        self.rate = rospy.Rate(1)  # 1 Hz

    def run(self):
        while not rospy.is_shutdown():
          #   # Prompt user for the path selection
          #   selected_path = input("Enter the path to publish (e.g., 'path1', 'path2', 'path3'): ")
          #   rospy.loginfo(f"Publishing selected path: {selected_path}")
            
            # Publish the selected path
            self.path_pub.publish('path1')
            self.rate.sleep()

if __name__ == '__main__':
    try:
        path_selector_node = PathSelectorNode()
        path_selector_node.run()
    except rospy.ROSInterruptException:
        pass
