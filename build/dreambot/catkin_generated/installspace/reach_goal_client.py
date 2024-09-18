#!/usr/bin/env python3

import rospy
import actionlib
from std_msgs.msg import Bool
from dreambot.msg import ControlAction, ControlGoal  # Import the custom action messages

class CooperativeModeClient:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('cooperative_mode_client')

        # Create an action client for the ControlAction
        self.client = actionlib.SimpleActionClient('control_action', ControlAction)

        # Wait for the action server to start
        rospy.loginfo("Waiting for action server to start...")
        self.client.wait_for_server()
        rospy.loginfo("Action server started, ready to send goals.")

        # Subscribe to the cooperative_mode topic
        self.cooperative_mode_sub = rospy.Subscriber('cooperative_mode', Bool, self.cooperative_mode_callback)

        # State variable to keep track of the current mode
        self.current_mode = False

    def cooperative_mode_callback(self, msg):
        # Check the value of cooperative_mode and take action accordingly
        if msg.data and not self.current_mode:
            # Cooperative mode is True and not already started; send a start goal
            self.send_start_goal()
        elif not msg.data and self.current_mode:
            # Cooperative mode is False and action is running; cancel the goal
            self.send_stop_goal()

    def send_start_goal(self):
        # Create and send a start goal to the action server
        goal = ControlGoal()
        goal.start = True
        self.client.send_goal(goal, done_cb=self.done_callback)
        self.current_mode = True
        rospy.loginfo("Sent start goal to action server.")

    def send_stop_goal(self):
        # Cancel the current goal to stop the action
        self.client.cancel_goal()
        self.current_mode = False
        rospy.loginfo("Sent stop goal to action server.")

    def done_callback(self, status, result):
        # Callback function when the action completes
        if status == actionlib.GoalStatus.SUCCEEDED:
            rospy.loginfo("Action succeeded: {}".format(result.success))
        else:
            rospy.logwarn("Action did not succeed, status: {}".format(status))

if __name__ == '__main__':
    try:
        client = CooperativeModeClient()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
