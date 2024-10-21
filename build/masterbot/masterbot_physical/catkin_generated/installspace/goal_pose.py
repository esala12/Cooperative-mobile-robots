#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def goal_callback(msg):
    # Log the received message for debugging
    rospy.loginfo("Received goal: Position (%f, %f, %f), Orientation (%f, %f, %f, %f)",
                  msg.pose.position.x, msg.pose.position.y, msg.pose.position.z,
                  msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w)

    # Create a new PoseStamped message
    new_goal = PoseStamped()

    # Copy header
    new_goal.header.seq = msg.header.seq
    new_goal.header.stamp = msg.header.stamp
    new_goal.header.frame_id = msg.header.frame_id

    # Copy pose
    new_goal.pose.position = msg.pose.position
    new_goal.pose.orientation = msg.pose.orientation

    # Publish the new goal to the /master_move_base_simple/goal topic
    goal_pub.publish(new_goal)
    rospy.loginfo("Republished goal to /master_move_base_simple/goal")

def goal_republisher():
    # Initialize the ROS node
    rospy.init_node('goal_republisher', anonymous=True)

    # Create a subscriber to /move_base_simple/goal
    rospy.Subscriber('/move_base_simple/goal', PoseStamped, goal_callback)

    # Create a publisher to /master_move_base_simple/goal
    global goal_pub
    goal_pub = rospy.Publisher('/master_move_base_simple/goal', PoseStamped, queue_size=10)

    # Spin to keep the script for receiving and republishing goals
    rospy.spin()

if __name__ == '__main__':
    try:
        goal_republisher()
    except rospy.ROSInterruptException:
        pass
