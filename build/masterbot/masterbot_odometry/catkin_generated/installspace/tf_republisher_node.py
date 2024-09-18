#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage

def transform_callback(msg):
    
    for transform in msg.transforms:
        # Check if the transform is from master_base_footprint to master_base_link
        if transform.child_frame_id == "master_base_footprint":
            # Update the child frame ID to master_base_link
            transform.child_frame_id = "base_footprint_ekf"
        # Update the frame ID of the parent
        transform.header.frame_id = "master_base_link"  # Update to your desired parent frame
        # Publish the modified transform
        transform_pub.publish(TFMessage([transform]))

if __name__ == '__main__':
    rospy.init_node('tf_transform_node')
    
    # Subscriber to the /tf topic
    rospy.Subscriber('/tf', TFMessage, transform_callback)
    
    # Publisher for the modified transforms
    transform_pub = rospy.Publisher('/modified_tf', TFMessage, queue_size=10)
    
    rospy.spin()
