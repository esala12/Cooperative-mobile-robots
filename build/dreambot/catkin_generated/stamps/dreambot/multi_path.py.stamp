#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped
from dreambot_tkinter.msg import BoolString, BoolInt
from dreambot.msg import PathArray, CombinedPathStatus
from std_msgs.msg import Bool
import numpy as np
import math


class MultiPathSubscriberNode:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('multi_path_subscriber_node', anonymous=True)

        # Subscribe to the odometry topics
        self.slavebot_sub = rospy.Subscriber('/slave_filter', Odometry, self.slavebot_callback)
        self.masterbot_sub = rospy.Subscriber('/master_filter', Odometry, self.masterbot_callback)

        # Subscribe to the multi_path topic with BoolString message
        self.multi_path_sub = rospy.Subscriber('/multi_path', BoolString, self.multi_path_callback)
        self.activate_sub = rospy.Subscriber('/activate_base_station', BoolInt, self.activate_callback, queue_size=20)

        # Subscribe to the docking station topics
        self.master_docking_sub = rospy.Subscriber('/master_docking_station', Bool, self.master_docking_callback)
        self.slave_docking_sub = rospy.Subscriber('/slave_docking_station', Bool, self.slave_docking_callback)

        # Publisher for combined status message
        self.combined_status_pub = rospy.Publisher('/combined_path_status', CombinedPathStatus, queue_size=10)
        # Publisher for the /path topic
        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)

        # Coordinates
        self.initial_coordinate = [-8.8, 5.5]
        self.b_coordinate = [0, 5.5]
        self.c_coordinate = [9.5, 5.5]
        self.f_coordinate = [9.5, -1]
        self.d_coordinate = [-8.8, -1]
        self.e_coordinate = [0, -1]

        # Initialize variables
        self.slavebot_x = None
        self.slavebot_y = None
        self.masterbot_x = None
        self.masterbot_y = None
        self.half_dist = None
        self.corner_dist = None
        self.multi_path_state = {'flag': False, 'data': ''}
        self.path = Path()
        self.path.header.frame_id = "map"
        self.master_docking = False
        self.slave_docking = False
        self.multi_path_flag = False
        self.node_active = False

    def slavebot_callback(self, msg):
        self.slavebot_x = msg.pose.pose.position.x
        self.slavebot_y = msg.pose.pose.position.y
        self.update_path(msg)

    def masterbot_callback(self, msg):
        self.masterbot_x = msg.pose.pose.position.x
        self.masterbot_y = msg.pose.pose.position.y
        self.update_path(msg)

    def multi_path_callback(self, msg):
        self.multi_path_state['flag'] = msg.flag
        self.multi_path_state['data'] = msg.data
        self.multi_path_flag = msg.flag
        self.check_activation_condition()

    def activate_callback(self, msg):
        self.half_dist = msg.number / 2
        self.corner_dist = math.sqrt((msg.number ** 2) / 2)

    def master_docking_callback(self, msg):
        self.master_docking = msg.data
        self.check_activation_condition()

    def slave_docking_callback(self, msg):
        self.slave_docking = msg.data
        self.check_activation_condition()

    def check_activation_condition(self):
        if self.master_docking and self.slave_docking and self.multi_path_flag:
            self.node_active = True
            self.publish_combined_status()

    def update_path(self, odom_msg):
        pose_stamped = PoseStamped()
        pose_stamped.header = odom_msg.header
        pose_stamped.pose = odom_msg.pose.pose
        self.path.poses.append(pose_stamped)
        self.path.header.stamp = rospy.Time.now()

    def generate_combined_path(self):
        if self.multi_path_state['data'] == 'B':
            rospy.loginfo("Generating path for mode B.")
            num_points = 10000
            path1 = np.column_stack(
                (np.full(num_points, self.initial_coordinate[0]),
                np.linspace(self.slavebot_y, self.initial_coordinate[1]-1.5, num_points)))
            path2 = np.column_stack(
                (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0]+1.5, num_points), 
                np.linspace(self.initial_coordinate[1]-1.5, self.initial_coordinate[1], num_points) + 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path3 = np.column_stack(
                (np.linspace(self.initial_coordinate[0]+1.5, self.half_dist, num_points),
                np.full(num_points, self.initial_coordinate[1])))
            combined_path = np.vstack((path1, path2, path3))
            return combined_path

        # Add more paths according to the data string value
        elif self.multi_path_state['data'] == 'C':
            rospy.loginfo("Generating path for mode C.")
            num_points = 10000
            path1 = np.column_stack(
                (np.full(num_points, self.initial_coordinate[0]),
                np.linspace(self.slavebot_y, self.initial_coordinate[1] - 1.5, num_points)))
            path2 = np.column_stack(
                (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0] + 1.5, num_points),
                np.linspace(self.initial_coordinate[1] - 1.5, self.initial_coordinate[1], num_points) + 
                0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path3 = np.column_stack(
                (np.linspace(self.initial_coordinate[0] + 1.5, self.c_coordinate[0] - 1.5, num_points),
                np.full(num_points, self.initial_coordinate[1])))
            path4 = np.column_stack(
                (np.linspace(self.c_coordinate[0] - 1.5, self.c_coordinate[0], num_points),
                np.linspace(self.c_coordinate[1], self.initial_coordinate[1] - 1.5, num_points) + 
                0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path5 = np.column_stack(
                (np.full(num_points, self.c_coordinate[0]),
                np.linspace(self.c_coordinate[1]-1.5, self.c_coordinate[1] - self.corner_dist, num_points)))
            combined_path = np.vstack((path1, path2, path3, path4, path5))
            return combined_path
        
        elif self.multi_path_state['data'] == 'F':
            rospy.loginfo("Generating path for mode F.")
            num_points = 10000
            path1 = np.column_stack(
                (np.full(num_points, self.initial_coordinate[0]),
                np.linspace(self.slavebot_y, self.initial_coordinate[1]-1.5, num_points)))
            path2 = np.column_stack(
                (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0]+1.5, num_points), 
                np.linspace(self.initial_coordinate[1]-1.5, self.initial_coordinate[1], num_points) + 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path3 = np.column_stack(
                (np.linspace(self.initial_coordinate[0]+1.5, self.b_coordinate[0]-3, num_points),
                np.full(num_points, self.initial_coordinate[1])))
            path4 = np.column_stack(
                (np.linspace(self.b_coordinate[0] - 3, self.b_coordinate[0], num_points),
                np.linspace(self.b_coordinate[1], self.b_coordinate[1] - 3, num_points) + 
                0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path5 = np.column_stack(
                (np.linspace(self.b_coordinate[0] , self.b_coordinate[0]+3, num_points)-
                0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points)),
                np.linspace(self.b_coordinate[1]-3, self.f_coordinate[1], num_points) ))
            path6 = np.column_stack(
                (np.linspace(self.b_coordinate[0] + 3, self.f_coordinate[0] - 1.5, num_points),
                np.full(num_points, self.f_coordinate[1])))
            path7 = np.column_stack(
                (np.linspace(self.f_coordinate[0] - 1.5, self.f_coordinate[0], num_points),
                np.linspace(self.f_coordinate[1], self.f_coordinate[1] + 1.5, num_points) - 
                0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path8 = np.column_stack(
                (np.full(num_points, self.f_coordinate[0]),
                np.linspace(self.f_coordinate[1]+1.5, self.f_coordinate[1] + self.corner_dist, num_points)))
            combined_path = np.vstack((path1, path2, path3, path4, path5, path6, path7, path8))
            return combined_path
        
        elif self.multi_path_state['data'] == 'D':
            rospy.loginfo("Generating path for mode D")
            num_points = 10000
            path1 = np.column_stack(
                (np.linspace(self.masterbot_x, self.initial_coordinate[0]+1.5, num_points),
                np.full(num_points, self.initial_coordinate[1])))            
            path2 = np.column_stack(
                (np.linspace(self.initial_coordinate[0]+1.5, self.initial_coordinate[0], num_points), 
                np.linspace(self.initial_coordinate[1], self.initial_coordinate[1]-1.5, num_points) + 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path3 = np.column_stack(
                (np.full(num_points, self.d_coordinate[0]),
                np.linspace(self.initial_coordinate[1]-1.5, self.d_coordinate[1]+1.5, num_points)))
            path4 = np.column_stack(
                (np.linspace(self.d_coordinate[0], self.d_coordinate[0]+1.5, num_points), 
                np.linspace(self.d_coordinate[1]+1.5, self.d_coordinate[1], num_points) - 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path5 = np.column_stack(
                (np.linspace(self.d_coordinate[0]+1.5, self.d_coordinate[0]+self.corner_dist, num_points),
                np.full(num_points, self.d_coordinate[1])))   
            combined_path = np.vstack((path1, path2, path3, path4, path5))
            return combined_path
        
        elif self.multi_path_state['data'] == 'E':
            rospy.loginfo("Generating path for mode D")
            num_points = 10000
            path1 = np.column_stack(
                (np.linspace(self.masterbot_x, self.initial_coordinate[0]+1.5, num_points),
                np.full(num_points, self.initial_coordinate[1])))            
            path2 = np.column_stack(
                (np.linspace(self.initial_coordinate[0]+1.5, self.initial_coordinate[0], num_points), 
                np.linspace(self.initial_coordinate[1], self.initial_coordinate[1]-1.5, num_points) + 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path3 = np.column_stack(
                (np.full(num_points, self.d_coordinate[0]),
                np.linspace(self.initial_coordinate[1]-1.5, self.d_coordinate[1]+1.5, num_points)))
            path4 = np.column_stack(
                (np.linspace(self.d_coordinate[0], self.d_coordinate[0]+1.5, num_points), 
                np.linspace(self.d_coordinate[1]+1.5, self.d_coordinate[1], num_points) - 0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
            path5 = np.column_stack(
                (np.linspace(self.d_coordinate[0]+1.5, self.d_coordinate[0]+self.corner_dist, num_points),
                np.full(num_points, self.d_coordinate[1]))) 
            path6 = np.column_stack(
                (np.linspace(self.d_coordinate[0]+self.corner_dist, self.e_coordinate[0]+self.half_dist, num_points),
                np.full(num_points, self.e_coordinate[1])))     
            combined_path = np.vstack((path1, path2, path3, path4, path5, path6))
            return combined_path
        
        else:
            rospy.logwarn(f"Unsupported path mode: {self.multi_path_state['data']}. No path generated.")
            return None

    def publish_combined_status(self):
        if self.node_active:
            combined_path = self.generate_combined_path()
            path_published = False  # Default to False

            # Determine if the path being published is D or E
            if self.multi_path_state['data'] in ['D', 'E']:
                path_published = True

            # Create and populate the CombinedPathStatus message
            combined_status_msg = CombinedPathStatus()
            if combined_path is not None:
                combined_status_msg.path.x = combined_path[:, 0].tolist()
                combined_status_msg.path.y = combined_path[:, 1].tolist()

                # Publish the Path message using self.path_pub
                self.publish_path(combined_path)

            combined_status_msg.node_active = self.node_active
            combined_status_msg.path_published = path_published

            # Publish the combined status message
            self.combined_status_pub.publish(combined_status_msg)
            rospy.loginfo(f"Combined status for mode {self.multi_path_state['data']} published")

    def publish_path(self, combined_path):
        # Create a Path message to publish the combined path
        path_msg = Path()
        path_msg.header.frame_id = "map"
        path_msg.header.stamp = rospy.Time.now()

        # Convert combined path points to PoseStamped and add to path message
        for point in combined_path:
            pose_stamped = PoseStamped()
            pose_stamped.header.frame_id = "map"
            pose_stamped.header.stamp = rospy.Time.now()
            pose_stamped.pose.position.x = point[0]
            pose_stamped.pose.position.y = point[1]
            path_msg.poses.append(pose_stamped)

        # Publish the path message
        self.path_pub.publish(path_msg)
        rospy.loginfo("Path published successfully.")


if __name__ == '__main__':
    try:
        node = MultiPathSubscriberNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass