#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Pose, Twist, Point, Vector3
import tf
import math

class OdometryPublisher:
    def __init__(self):
        # Initialize the node
        rospy.init_node('odometry_publisher', anonymous=True)
        
        # Subscribe to the /masterbot_kalman topic
        self.vel_sub = rospy.Subscriber('/masterbot_kalman', Odometry, self.velocity_callback)
        
        # Publisher for odometry
        self.odom_pub = rospy.Publisher('/master_odom_cal', Odometry, queue_size=10)

        # TF broadcaster for broadcasting odometry as a transform
        self.odom_broadcaster = tf.TransformBroadcaster()
        
        # Parameters for robot state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        
        # Previous timestamp for calculating delta time
        self.last_time = rospy.Time.now()

    def velocity_callback(self, msg):
        # Get the current time
        current_time = rospy.Time.now()

        # Velocities from the Odometry message
        vx = msg.twist.twist.linear.x  # Forward velocity
        vy = msg.twist.twist.linear.y  # Lateral velocity
        vtheta = msg.twist.twist.angular.z  # Angular velocity

        # Calculate time delta
        dt = (current_time - self.last_time).to_sec()

        # Update robot's position and orientation using the velocities
        delta_x = (vx * math.cos(self.theta) - vy * math.sin(self.theta)) * dt
        delta_y = (vx * math.sin(self.theta) + vy * math.cos(self.theta)) * dt
        delta_theta = vtheta * dt

        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

        # Normalize theta to be within -pi to pi
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

        # Publish the odometry message
        self.publish_odometry(current_time, vx, vy, vtheta)

        # Publish the TF transform
        self.publish_tf(current_time)

        # Update the last time for the next iteration
        self.last_time = current_time

    def publish_odometry(self, current_time, vx, vy, vtheta):
        # Create odometry message
        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = 'master_odom_cal'
        
        # Set the position
        odom.pose.pose = Pose(Point(self.x, self.y, 0.0), 
                              Quaternion(*tf.transformations.quaternion_from_euler(0, 0, self.theta)))

        # Set the velocity
        odom.child_frame_id = 'master_base_footprint_cal'
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vtheta))

        # Publish the message
        self.odom_pub.publish(odom)

    def publish_tf(self, current_time):
        # Broadcast the transform between odom and base_footprint
        self.odom_broadcaster.sendTransform(
            (self.x, self.y, 0),  # Translation: x, y, z (z is 0 because it's a 2D robot)
            tf.transformations.quaternion_from_euler(0, 0, self.theta),  # Rotation in quaternion (roll, pitch, yaw)
            current_time,  # Timestamp
            "master_base_footprint_cal",  # Child frame (base of the robot)
            "master_odom_cal"  # Parent frame (odometry frame)
        )

if __name__ == '__main__':
    try:
        odom_pub = OdometryPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
