#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray

# Define robot-specific constants
lx = 0.37  # Distance from the center of the robot to the wheels in x direction (meters) 0.39(original)
ly = 0.38  # Distance from the center of the robot to the wheels in y direction (meters) 0.36
r = 0.04   # Wheel radius (meters)
MAX_RPM = 50  # Maximum allowed RPM

# Publisher for the wheel RPMs
rpm_pub = None

def clamp_rpm(rpm):
    """Clamp the RPM value to be within the allowed maximum."""
    return max(min(rpm, MAX_RPM), -MAX_RPM)  # Clamp both positive and negative RPM

def cmd_vel_callback(msg):
    # Extract velocities from the Twist message
    vx = msg.linear.x
    vy = msg.linear.y
    wz = msg.angular.z

    # Compute common term lx + ly
    lx_ly = lx + ly

    # Matrix multiplication to compute wheel angular velocities (rad/s)
    w_fl = (1 / r) * (vx - vy - lx_ly * wz)
    w_fr = (1 / r) * (vx + vy + lx_ly * wz)
    w_rl = (1 / r) * (vx + vy - lx_ly * wz)
    w_rr = (1 / r) * (vx - vy + lx_ly * wz)

    # Convert angular velocity (rad/s) to RPM
    rpm_fl = w_fl * (60 / (2 * 3.1416))
    rpm_fr = w_fr * (60 / (2 * 3.1416))
    rpm_rl = w_rl * (60 / (2 * 3.1416))
    rpm_rr = w_rr * (60 / (2 * 3.1416))

    # Clamp the RPM values to the maximum allowed RPM
    rpm_fl = clamp_rpm(rpm_fl)
    rpm_fr = clamp_rpm(rpm_fr)
    rpm_rl = clamp_rpm(rpm_rl)
    rpm_rr = clamp_rpm(rpm_rr)

    # Log the RPMs for debugging
    rospy.loginfo(f"Motor RPMs -> Front Left: {rpm_fl}, Front Right: {rpm_fr}, Rear Left: {rpm_rl}, Rear Right: {rpm_rr}")

    # Publish the RPMs in a Float32MultiArray
    rpm_msg = Float32MultiArray()
    rpm_msg.data = [rpm_fr, rpm_fl, rpm_rl, rpm_rr]
    rpm_pub.publish(rpm_msg)

def listener():
    global rpm_pub
    # Initialize the ROS node
    rospy.init_node('master_cmd_vel_listener', anonymous=True)
    
    # Subscribe to the /master_cmd_vel topic
    rospy.Subscriber("/master_cmd_vel", Twist, cmd_vel_callback)
    
    # Initialize the RPM publisher
    rpm_pub = rospy.Publisher('/wheel_velocities_master', Float32MultiArray, queue_size=10)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    listener()
