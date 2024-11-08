#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import numpy as np

class PathGeneratorNode:
    def __init__(self):
        self.path_pub = rospy.Publisher('/generated_path', Path, queue_size=10)
        self.rate = rospy.Rate(1)  # 1 Hz publishing rate

        self.initial_coordinate = [-0.3, 0.3]
        self.b_coordinate = [3.5, 0.3]
        self.c_coordinate = [7.5, 0.3]
        self.f_coordinate = [7.5, -4.5]
        self.d_coordinate = [-0.3, -4.5]
        self.e_coordinate = [3.5, -4.5]
        self.slavebot_y = -2.0
        self.half_dist = 2.0
        self.corner_dist = 2.0
        self.masterbot_x = 2.0

    def generate_path(self):
        # Path generation logic from the original code


        # num_points = 10000
        # path1 = np.column_stack(
        #     (np.full(num_points, self.initial_coordinate[0]),
        #     np.linspace(self.slavebot_y, self.initial_coordinate[1]-1.0, num_points)))
        # path2 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0]+1.0, num_points), 
        #     np.linspace(self.initial_coordinate[1]-1.0, self.initial_coordinate[1], num_points) + 0.4 * np.sin(0.8 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path3 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0]+1.0, self.b_coordinate[0]+self.half_dist, num_points),
        #     np.full(num_points, self.initial_coordinate[1])))
        # combined_path = np.vstack((path1, path2, path3))
        # return combined_path

        # num_points = 10000
        # path1 = np.column_stack(
        #     (np.full(num_points, self.initial_coordinate[0]),
        #     np.linspace(self.slavebot_y, self.initial_coordinate[1] - 1.0, num_points)))
        # path2 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0] + 1.0, num_points),
        #     np.linspace(self.initial_coordinate[1] - 1.0, self.initial_coordinate[1], num_points) + 
        #     0.4 * np.sin(0.8 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path3 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0] + 1.0, self.c_coordinate[0] - 1.0, num_points),
        #     np.full(num_points, self.initial_coordinate[1])))
        # path4 = np.column_stack(
        #     (np.linspace(self.c_coordinate[0] - 1.0, self.c_coordinate[0], num_points),
        #     np.linspace(self.c_coordinate[1], self.initial_coordinate[1] - 1.0, num_points) + 
        #     0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path5 = np.column_stack(
        #     (np.full(num_points, self.c_coordinate[0]),
        #     np.linspace(self.c_coordinate[1]-1.0, self.c_coordinate[1] - self.corner_dist, num_points)))
        # combined_path = np.vstack((path1, path2, path3, path4, path5))
        # return combined_path

        # num_points = 10000
        # path1 = np.column_stack(
        #     (np.full(num_points, self.initial_coordinate[0]),
        #     np.linspace(self.slavebot_y, self.initial_coordinate[1]-1.0, num_points)))
        # path2 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0], self.initial_coordinate[0]+1.0, num_points), 
        #     np.linspace(self.initial_coordinate[1]-1.0, self.initial_coordinate[1], num_points) + 0.4 * np.sin(0.8 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path3 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0]+1.0, self.b_coordinate[0]-1.0, num_points),
        #     np.full(num_points, self.initial_coordinate[1])))
        # path4 = np.column_stack(
        #     (np.linspace(self.b_coordinate[0] - 1.0, self.b_coordinate[0], num_points),
        #     np.linspace(self.b_coordinate[1], self.b_coordinate[1] - 2, num_points)+ 
        #     0.4 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path5 = np.column_stack(
        #     (np.linspace(self.b_coordinate[0] , self.b_coordinate[0]+1, num_points)-
        #     0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points)),
        #     np.linspace(self.b_coordinate[1]-2, self.f_coordinate[1], num_points) ))
        # path6 = np.column_stack(
        #     (np.linspace(self.b_coordinate[0] + 1, self.f_coordinate[0] - 1.0, num_points),
        #     np.full(num_points, self.f_coordinate[1])))
        # path7 = np.column_stack(
        #     (np.linspace(self.f_coordinate[0] - 1.0, self.f_coordinate[0], num_points),
        #     np.linspace(self.f_coordinate[1], self.f_coordinate[1] + 1.0, num_points) - 
        #     0.2 * np.sin(1.0 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path8 = np.column_stack(
        #     (np.full(num_points, self.f_coordinate[0]),
        #     np.linspace(self.f_coordinate[1]+1.0, self.f_coordinate[1] + self.corner_dist, num_points)))
        # combined_path = np.vstack((path1, path2, path3, path4, path5, path6, path7, path8))
        # return combined_path

        # num_points = 10000
        # path1 = np.column_stack(
        #     (np.linspace(self.masterbot_x, self.initial_coordinate[0]+1.0, num_points),
        #     np.full(num_points, self.initial_coordinate[1])))            
        # path2 = np.column_stack(
        #     (np.linspace(self.initial_coordinate[0]+1.0, self.initial_coordinate[0], num_points), 
        #     np.linspace(self.initial_coordinate[1], self.initial_coordinate[1]-1.0, num_points) + 0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path3 = np.column_stack(
        #     (np.full(num_points, self.d_coordinate[0]),
        #     np.linspace(self.initial_coordinate[1]-1.0, self.d_coordinate[1]+1.0, num_points)))
        # path4 = np.column_stack(
        #     (np.linspace(self.d_coordinate[0], self.d_coordinate[0]+1.0, num_points), 
        #     np.linspace(self.d_coordinate[1]+1.0, self.d_coordinate[1], num_points) - 0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        # path5 = np.column_stack(
        #     (np.linspace(self.d_coordinate[0]+1.0, self.d_coordinate[0]+self.corner_dist, num_points),
        #     np.full(num_points, self.d_coordinate[1])))   
        # combined_path = np.vstack((path1, path2, path3, path4, path5))
        # return combined_path

        num_points = 10000
        path1 = np.column_stack(
            (np.linspace(self.masterbot_x, self.initial_coordinate[0]+1.0, num_points),
            np.full(num_points, self.initial_coordinate[1])))            
        path2 = np.column_stack(
            (np.linspace(self.initial_coordinate[0]+1.0, self.initial_coordinate[0], num_points), 
            np.linspace(self.initial_coordinate[1], self.initial_coordinate[1]-1.0, num_points) + 0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path3 = np.column_stack(
            (np.full(num_points, self.d_coordinate[0]),
            np.linspace(self.initial_coordinate[1]-1.0, self.d_coordinate[1]+1.0, num_points)))
        path4 = np.column_stack(
            (np.linspace(self.d_coordinate[0], self.d_coordinate[0]+1.0, num_points), 
            np.linspace(self.d_coordinate[1]+1.0, self.d_coordinate[1], num_points) - 0.2 * np.sin(1 * np.pi / 3 * np.linspace(3, 0, num_points))))
        path5 = np.column_stack(
            (np.linspace(self.d_coordinate[0]+1.0, self.d_coordinate[0]+self.corner_dist, num_points),
            np.full(num_points, self.d_coordinate[1]))) 
        path6 = np.column_stack(
            (np.linspace(self.d_coordinate[0]+self.corner_dist, self.e_coordinate[0]+self.half_dist, num_points),
            np.full(num_points, self.e_coordinate[1])))     
        combined_path = np.vstack((path1, path2, path3, path4, path5, path6))
        return combined_path

        

    def publish_path(self):
        path_points = self.generate_path()

        path_msg = Path()
        path_msg.header.stamp = rospy.Time.now()
        path_msg.header.frame_id = "map"

        for point in path_points:
            pose = PoseStamped()
            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "map"
            pose.pose.position.x = point[0]
            pose.pose.position.y = point[1]
            pose.pose.position.z = 0
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0
            path_msg.poses.append(pose)

        self.path_pub.publish(path_msg)

    def run(self):
        while not rospy.is_shutdown():
            self.publish_path()
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('path_generator_node')
    path_generator = PathGeneratorNode()
    path_generator.run()
