#!/usr/bin/env python3

import rospy
import tf
from nav_msgs.msg import Odometry

class TfListener(object):
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('tf_listener_node')
        
        # Create a TransformListener object
        self.listener = tf.TransformListener()
        
        # Set up a timer to periodically check for transforms
        self.timer = rospy.Timer(rospy.Duration(0.1), self.timer_callback)  # Change to 0.1 seconds for 10 Hz frequency
        
        # Create Odometry publishers
        self.odom_pub_master = rospy.Publisher('master_filter', Odometry, queue_size=10)
        self.odom_pub_slave = rospy.Publisher('slave_filter', Odometry, queue_size=10)
    
    def timer_callback(self, event):
        try:
            # Look up the transform from 'map' to 'master_base_footprint_ekf'
            (trans_master, rot_master) = self.listener.lookupTransform('map', 'master_base_footprint_ekf', rospy.Time(0))
            # Create and publish the Odometry message for the master
            odom_master = Odometry()
            odom_master.header.stamp = rospy.Time.now()
            odom_master.header.frame_id = 'map'
            odom_master.child_frame_id = 'master_base_footprint_ekf'
            odom_master.pose.pose.position.x = trans_master[0]
            odom_master.pose.pose.position.y = trans_master[1]
            odom_master.pose.pose.position.z = trans_master[2]
            odom_master.pose.pose.orientation.x = rot_master[0]
            odom_master.pose.pose.orientation.y = rot_master[1]
            odom_master.pose.pose.orientation.z = rot_master[2]
            odom_master.pose.pose.orientation.w = rot_master[3]
            self.odom_pub_master.publish(odom_master)
            
            # Look up the transform from 'map' to 'slave_base_footprint_ekf'
            (trans_slave, rot_slave) = self.listener.lookupTransform('map', 'slave_base_footprint_ekf', rospy.Time(0))
            # Create and publish the Odometry message for the slave
            odom_slave = Odometry()
            odom_slave.header.stamp = rospy.Time.now()
            odom_slave.header.frame_id = 'map'
            odom_slave.child_frame_id = 'slave_base_footprint_ekf'
            odom_slave.pose.pose.position.x = trans_slave[0]
            odom_slave.pose.pose.position.y = trans_slave[1]
            odom_slave.pose.pose.position.z = trans_slave[2]
            odom_slave.pose.pose.orientation.x = rot_slave[0]
            odom_slave.pose.pose.orientation.y = rot_slave[1]
            odom_slave.pose.pose.orientation.z = rot_slave[2]
            odom_slave.pose.pose.orientation.w = rot_slave[3]
            self.odom_pub_slave.publish(odom_slave)
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            rospy.logerr("Error looking up transform: %s", e)

if __name__ == '__main__':
    try:
        TfListener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
