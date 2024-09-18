#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Point

class MoveBaseClient:
    def __init__(self):
        self.ac = actionlib.SimpleActionClient("master_move_base", MoveBaseAction)
        rospy.init_node('masterbot_navigation', anonymous=False)
        self.wait_for_server()

    def wait_for_server(self):
        rospy.loginfo("Waiting for the move_base action server to come up")
        self.ac.wait_for_server()

    def move_to_goal(self, nextGoal):
        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position = Point(nextGoal[0], nextGoal[1], 0)
        goal.target_pose.pose.orientation.z = nextGoal[2]
        goal.target_pose.pose.orientation.w = nextGoal[3]

        rospy.loginfo("Sending goal location ....")
        self.ac.send_goal(goal)

        self.ac.wait_for_result(rospy.Duration(60))

        if self.ac.get_state() == GoalStatus.SUCCEEDED:
            rospy.loginfo("You have reached the destination")
            return True
        else:
            rospy.loginfo("The robot failed to reach the destination")
            return False

    def next_goal(self, next):
        A = [-7.8346428871154785, 5.331421852111816, -0.9472726148373964, 0.3204287645938198]
        B = [-8.117826461791992, -0.2288515567779541, -0.31909745853894544, 0.9477219064440718]
        C = [0.058264344930648804, -0.5612173080444336, 0.004372066393586199, 0.9999904424720518]
        D = [8.511659622192383, -0.5820822715759277, 0.34903015262020504, 0.9371114942000852]
        E = [8.906157493591309, 4.85897970199585, 0.9415708569313761, 0.336814966083032]
        F = [0.2109229564666748, 5.1971893310546875, 0.9999762828291153, 0.006887218543443463]
        Goals = [D, E, F, A, B, C,]
        return Goals[next]

if __name__ == '__main__':
    client = MoveBaseClient()
    next = 0

    while not rospy.is_shutdown():
        client.wait_for_server()
        nextGoal = client.next_goal(next)
        rospy.loginfo("Starting to go to goal")
        finish = client.move_to_goal(nextGoal)

        if finish:
            next += 1
            if next == 6:
                next = 0

    rospy.spin()
