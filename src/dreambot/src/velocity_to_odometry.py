#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Quaternion, Pose, Twist, Point, Vector3
import tf
import math

class OdometryPublisher:
    def __init__(self):
        # Initialize the node
        rospy.init_node('odometry_publisher', anonymous=True)
        
        # Subscribe to the velocity topic
        self.vel_sub = rospy.Subscriber('/current_robot_velocity', Float32MultiArray, self.velocity_callback)
        
        # Publisher for odometry
        self.odom_pub = rospy.Publisher('/master_odom_cal', Odometry, queue_size=10)
        
        
        # Parameters for robot state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        
        # Previous timestamp for calculating delta time
        self.last_time = rospy.Time.now()

    def velocity_callback(self, msg):
        # Get the current time
        current_time = rospy.Time.now()

        # Velocities from the message (assumes the message contains [vx, vy, vtheta])
        vx = msg.data[0]
        vy = msg.data[1]
        vtheta = msg.data[2]

        # Calculate time delta
        dt = (current_time - self.last_time).to_sec()

        # Update robot's position and orientation using the velocities
        delta_x = (vx * math.cos(self.theta) - vy * math.sin(self.theta)) * dt
        delta_y = (vx * math.sin(self.theta) + vy * math.cos(self.theta)) * dt
        delta_theta = (-vtheta*2) * dt
        

        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

        # Normalize theta to be within -pi to pi
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

        # Publish the odometry message
        self.publish_odometry(current_time, vx, vy, vtheta)

        # Update the last time for the next iteration
        self.last_time = current_time

    def publish_odometry(self, current_time, vx, vy, vtheta):
        # Create odometry message
        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = 'odom'
        
        # Set the position
        odom.pose.pose = Pose(Point(self.x, self.y, 0.0), 
                              Quaternion(*tf.transformations.quaternion_from_euler(0, 0, self.theta)))

        # Set the velocity
        odom.child_frame_id = 'base_link'
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vtheta))

        # Publish the message
        self.odom_pub.publish(odom)

if __name__ == '__main__':
    try:
        odom_pub = OdometryPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass