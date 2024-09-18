#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
import tf

class PoseSubscriber:
    def __init__(self):
        rospy.init_node('pose_subscriber', anonymous=True)
        self.subscriber = rospy.Subscriber('/initialpose', PoseWithCovarianceStamped, self.pose_callback)
        rospy.spin()

    def pose_callback(self, msg):
        pose = msg.pose.pose
        x = pose.position.x
        y = pose.position.y

        orientation_q = pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, theta) = tf.transformations.euler_from_quaternion(orientation_list)

        rospy.loginfo("Received Pose: x = %f, y = %f, theta = %f", x, y, theta)

if __name__ == '__main__':
    try:
        PoseSubscriber()
    except rospy.ROSInterruptException:
        pass
