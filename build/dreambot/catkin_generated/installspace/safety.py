#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path, Odometry
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import tf
import numpy as np


class PathSafetyMonitorNode:
    def __init__(self):
        rospy.init_node('path_safety_monitor_node', anonymous=True)

        # Parameters
        self.path_buffer = 0.5  # Safety corridor width (meters)

        # Subscribers
        self.path_sub = rospy.Subscriber('/path', Path, self.path_callback)
        self.master_scan_sub = rospy.Subscriber('/master_scan', LaserScan, self.scan_callback)
        self.master_filter_sub = rospy.Subscriber('/master_filter', Odometry, self.odometry_callback)

        # Publisher
        self.safety_pub = rospy.Publisher('/safety', Bool, queue_size=10)

        # TF Listener
        self.tf_listener = tf.TransformListener()

        # Data storage
        self.current_path = None
        self.current_odometry = None
        self.safety_active = False

    def path_callback(self, msg):
        """Callback for the /path topic."""
        rospy.loginfo("Received Path message.")
        self.current_path = msg

    def odometry_callback(self, msg):
        """Callback for the /master_filter topic."""
        rospy.loginfo("Received Odometry message.")
        self.current_odometry = msg

    def scan_callback(self, msg):
        """Callback for the /master_scan topic."""
        rospy.loginfo("Received LaserScan message.")

        # Ensure all necessary data is available
        if self.current_path is None or self.current_odometry is None:
            rospy.logwarn("Path or Odometry data is missing. Skipping scan evaluation.")
            return

        # Transform laser scan points to map frame
        try:
            (trans, rot) = self.tf_listener.lookupTransform(
                "map", msg.header.frame_id, rospy.Time(0)
            )
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.logwarn("Failed to transform laser scan to map frame.")
            return

        scan_points = self.transform_scan_points(msg, trans, rot)
        if scan_points is None:
            rospy.logwarn("No valid scan points after transformation.")
            return

        # Check if any scan points lie within the safety corridor around the path
        obstacle_detected = self.check_obstacles_within_path(scan_points)

        # Publish safety status
        safety_msg = Bool()
        safety_msg.data = obstacle_detected

        if obstacle_detected and not self.safety_active:
            rospy.logwarn("Obstacle detected within path! Activating safety.")
        elif not obstacle_detected and self.safety_active:
            rospy.loginfo("Path is clear. Safety condition cleared.")

        self.safety_active = obstacle_detected
        self.safety_pub.publish(safety_msg)

    def transform_scan_points(self, scan_msg, trans, rot):
        """Transform laser scan points to the map frame."""
        angle_min = scan_msg.angle_min
        angle_increment = scan_msg.angle_increment
        ranges = np.array(scan_msg.ranges)

        # Filter valid ranges
        valid_indices = np.where((ranges > 0.0) & (ranges < scan_msg.range_max))
        ranges = ranges[valid_indices]
        angles = angle_min + angle_increment * valid_indices[0]

        # Convert to Cartesian coordinates in robot frame
        x_robot = ranges * np.cos(angles)
        y_robot = ranges * np.sin(angles)

        # Transform to map frame
        map_points = []
        for x, y in zip(x_robot, y_robot):
            point_in_map = self.transform_point([x, y, 0.0], trans, rot)
            if point_in_map is not None:
                map_points.append(point_in_map[:2])  # Only x, y coordinates
        return np.array(map_points)

    def transform_point(self, point, trans, rot):
        """Transform a point from the robot frame to the map frame."""
        try:
            # Create homogeneous point in robot frame
            point_homogeneous = np.array([point[0], point[1], point[2], 1.0])

            # Transformation matrix
            translation = np.array(trans)
            rotation = tf.transformations.quaternion_matrix(rot)
            transform_matrix = rotation.copy()
            transform_matrix[:3, 3] = translation

            # Transform point
            point_in_map = np.dot(transform_matrix, point_homogeneous)
            return point_in_map[:3]
        except Exception as e:
            rospy.logwarn(f"Error in transforming point: {e}")
            return None

    def check_obstacles_within_path(self, scan_points):
        """Check if any scan points lie within the safety corridor around the path."""
        for pose in self.current_path.poses:
            path_point = np.array([pose.pose.position.x, pose.pose.position.y])
            distances = np.linalg.norm(scan_points - path_point, axis=1)
            if np.any(distances < self.path_buffer):
                return True  # Obstacle detected
        return False


if __name__ == '__main__':
    try:
        node = PathSafetyMonitorNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
