#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
import tf

class OdomTFBroadcaster:
    def __init__(self):
        # Initialize the node
        rospy.init_node('master_tf_cal', anonymous=True)
        
        # Subscribe to the odometry topic
        self.odom_sub = rospy.Subscriber('/master_odom_cal', Odometry, self.odom_callback)
        
        # Create a TransformBroadcaster object
        self.tf_broadcaster = tf.TransformBroadcaster()

    def odom_callback(self, msg):
        # Extract position and orientation from the odometry message
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation

        # Publish the transformation from odom to base_link
        self.tf_broadcaster.sendTransform(
            (position.x, position.y, position.z),
            (orientation.x, orientation.y, orientation.z, orientation.w),
            rospy.Time.now(),
            "base_footprint",  # Child frame
            "odom"        # Parent frame
        )

if __name__ == '__main__':
    try:
        # Instantiate the broadcaster and start listening
        broadcaster = OdomTFBroadcaster()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
