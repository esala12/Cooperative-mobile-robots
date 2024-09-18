#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool, String

def parameter_publisher():
    rospy.init_node('parameter_publisher')

    # Publishers for parameters
    forward_slave_goal_pub = rospy.Publisher('/forward_slave_goal', Bool, queue_size=10)
    path_choice_pub = rospy.Publisher('/path_choice', String, queue_size=10)

    rate = rospy.Rate(1)  # Publish at 1 Hz

    # Initialize with default values
    forward_slave_goal = False
    path_choice = 'path2'

    while not rospy.is_shutdown():
        # Publish the parameters
        forward_slave_goal_pub.publish(forward_slave_goal)
        path_choice_pub.publish(path_choice)

        rospy.loginfo(f"Publishing forward_slave_goal: {forward_slave_goal}, path_choice: {path_choice}")

        # Here, you can add logic to change these values over time or based on input

        rate.sleep()

if __name__ == '__main__':
    try:
        parameter_publisher()
    except rospy.ROSInterruptException:
        pass
