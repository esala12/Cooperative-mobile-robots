#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Point
from dreambot_tkinter.msg import BoolInt
from std_msgs.msg import Bool
import math

class MoveBaseClient:
    def __init__(self):
        self.ac = actionlib.SimpleActionClient("master_move_base", MoveBaseAction)
        rospy.init_node('masterbot_navigation', anonymous=False)

        # Subscribe to the activate_base_station topic with BoolInt message type
        self.activate_sub = rospy.Subscriber('/activate_base_station', BoolInt, self.activate_callback, queue_size=20)

        # Publisher for master_docking_station topic
        self.docking_pub = rospy.Publisher('/master_docking_station', Bool, queue_size=10)

        # self.initial_coordinate = [-0.35, 0.3]
        # self.initial_coordinate = [-8.8, 5.5]
        self.initial_coordinate = [-0.3, 0.3]

        # Internal state to track if the robot should move
        self.active = False
        self.distance = 0
        self.master_pos = 0

        rospy.loginfo("Waiting for the move_base action server to come up")
        self.ac.wait_for_server()

    def activate_callback(self, msg):
        self.distance = msg.number
        half_dist = math.sqrt((self.distance ** 2) / 2)
        self.master_pos = self.initial_coordinate[0] + half_dist
        # Callback to handle the activate_base_station messages
        if msg.flag:
            rospy.loginfo(f"activate_base_station is True, activating movement with number {msg.number}")
            self.active = True
        else:
            rospy.loginfo(f"activate_base_station is False, stopping movement with number {msg.number}")
            self.active = False

    def move_to_goal(self, nextGoal):
        # Cancel any existing goals before sending a new one
        # self.docking_pub.publish(False)
        self.ac.cancel_all_goals()

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
            self.docking_pub.publish(True)  # Publish True when the goal is reached
            return True
        # else:
        #     rospy.loginfo("The robot failed to reach the destination")
        #     self.docking_pub.publish(False)  # Publish False when the goal is not reached
        #     return False

    def next_goal(self, next):
        return [self.master_pos, self.initial_coordinate[1], 0.004372066393586199, 0.9999904424720518]

    def run(self):
        next = 0
        while not rospy.is_shutdown():
            # Ensure the action server is ready
            if not self.ac.wait_for_server(timeout=rospy.Duration(5)):
                rospy.logwarn("Move base action server not available, waiting...")
                continue

            if self.active:  # Check if the node is activated
                rospy.loginfo("Starting to go to goal")
                nextGoal = self.next_goal(next)
                finish = self.move_to_goal(nextGoal)

                if finish:
                    next += 1
                    if next == 6:
                        next = 0
            else:
                rospy.loginfo("Waiting for activation...")

            rospy.sleep(1)  # Small delay to avoid busy waiting

if __name__ == '__main__':
    client = MoveBaseClient()
    client.run()
