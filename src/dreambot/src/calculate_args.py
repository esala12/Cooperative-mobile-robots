#!/usr/bin/env python3

import rospy
import roslaunch
import math

# Initialize a ROS node
rospy.init_node('arg_calculator', anonymous=True)

# Perform calculations
distance_object = 3.0
half_dist = math.sqrt((distance_object ** 2) / 2)
slave_pos = 5.5 - half_dist
master_pos = -9 + half_dist

# Set parameters directly in the ROS parameter server
rospy.set_param('/slave_pos', slave_pos)
rospy.set_param('/master_pos', master_pos)

# Log calculated values
rospy.loginfo(f"Calculated slave_pos: {slave_pos}")
rospy.loginfo(f"Calculated master_pos: {master_pos}")

# Launch nodes using roslaunch
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

# Specify the launch file and any additional arguments if needed
launch_file = "/home/esala/dreambot_ws/src/dreambot/launch/dreambot_fuzzy_navigation.launch"
launch_args = []

# Set up the launch parent to start the main launch file
parent = roslaunch.parent.ROSLaunchParent(uuid, [(launch_file, launch_args)])

try:
    # Start the launch file
    rospy.loginfo("Starting Dreambot launch...")
    parent.start()
    rospy.spin()  # Keep the script running
except Exception as e:
    rospy.logerr(f"Error during launch: {e}")
finally:
    rospy.loginfo("Shutting down Dreambot...")
    parent.shutdown()
