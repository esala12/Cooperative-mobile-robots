#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math  # Import the math module for trigonometric functions

class KalmanFilter(object):

     def __init__(self):
          self.odom_sub_ = rospy.Subscriber("/master_odom_cal", Odometry, self.odomCallback)
          self.imu_sub_ = rospy.Subscriber("/imu/data", Imu, self.imuCallback)
          self.odom_pub_ = rospy.Publisher("/masterbot_kalman", Odometry, queue_size=10)

          # Kalman filter variables
          self.mean_angular_z_ = 0.0
          self.variance_angular_z_ = 1000.0
          self.imu_angular_z_ = 0.0
          self.imu_accel_x_ = 0.0
          self.imu_accel_y_ = 0.0
          self.linear_velocity_x_ = 0.0
          self.linear_velocity_y_ = 0.0
          self.is_first_odom_ = True
          self.last_angular_z_ = 0.0
          self.last_time_ = rospy.Time.now()
          self.motion_variance_angular_ = 4.0
          self.motion_variance_linear_ = 4.0
          self.measurement_variance_angular_ = 0.5
          self.measurement_variance_linear_ = 0.5

          # Robot state
          self.x_ = 0.0
          self.y_ = 0.0
          self.theta_ = 0.0

          self.kalman_odom_ = Odometry()
          self.kalman_odom_.header.frame_id = "master_odom_kalman"
          self.kalman_odom_.child_frame_id = "master_base_footprint_kalman"

     def imuCallback(self, imu):
          self.imu_angular_z_ = imu.angular_velocity.z
          self.imu_accel_x_ = imu.linear_acceleration.x
          self.imu_accel_y_ = imu.linear_acceleration.y
          

     def odomCallback(self, odom):
          current_time = rospy.Time.now()
          delta_time = (current_time - self.last_time_).to_sec()

          if self.is_first_odom_:
               self.mean_angular_z_ = odom.twist.twist.angular.z
               self.last_angular_z_ = odom.twist.twist.angular.z
               self.is_first_odom_ = False
               self.last_time_ = current_time
               return

          # Integrate IMU accelerations to get velocities
          self.linear_velocity_x_ += self.imu_accel_x_ * delta_time
          self.linear_velocity_y_ += self.imu_accel_y_ * delta_time

          # Angular velocity Kalman filter
          self.motion_angular = odom.twist.twist.angular.z - self.last_angular_z_
          self.statePredictionAngular()
          self.measurementUpdateAngular()

          # Linear velocity Kalman filter
          self.statePredictionLinear(odom.twist.twist.linear.x, odom.twist.twist.linear.y)
          self.measurementUpdateLinear()

          # Update robot's position and orientation
          self.updateOdometry(delta_time)

          # Update the odometry message with filtered values
          self.kalman_odom_.twist.twist.angular.z = self.mean_angular_z_
          self.kalman_odom_.twist.twist.linear.x = self.linear_velocity_x_
          self.kalman_odom_.twist.twist.linear.y = self.linear_velocity_y_

          self.kalman_odom_.pose.pose.position.x = self.x_
          self.kalman_odom_.pose.pose.position.y = self.y_

          # Convert theta to quaternion
          quat = quaternion_from_euler(0, 0, self.theta_)
          self.kalman_odom_.pose.pose.orientation.x = quat[0]
          self.kalman_odom_.pose.pose.orientation.y = quat[1]
          self.kalman_odom_.pose.pose.orientation.z = quat[2]
          self.kalman_odom_.pose.pose.orientation.w = quat[3]

          # Publish the updated odometry
          self.odom_pub_.publish(self.kalman_odom_)

          self.last_angular_z_ = odom.twist.twist.angular.z
          self.last_time_ = current_time

     def measurementUpdateAngular(self):
          self.mean_angular_z_ = (self.measurement_variance_angular_ * self.mean_angular_z_ + self.variance_angular_z_ * self.imu_angular_z_) / (self.variance_angular_z_ + self.measurement_variance_angular_)
          self.variance_angular_z_ = (self.variance_angular_z_ * self.measurement_variance_angular_) / (self.variance_angular_z_ + self.measurement_variance_angular_)

     def statePredictionAngular(self):
          self.mean_angular_z_ = self.mean_angular_z_ + self.motion_angular
          self.variance_angular_z_ = self.variance_angular_z_ + self.motion_variance_angular_

     def measurementUpdateLinear(self):
          # Measurement update for linear velocities using odometry and IMU-derived velocity
          self.linear_velocity_x_ = (self.measurement_variance_linear_ * self.linear_velocity_x_ + self.motion_variance_linear_ * self.kalman_odom_.twist.twist.linear.x) / (self.motion_variance_linear_ + self.measurement_variance_linear_)
          self.linear_velocity_y_ = (self.measurement_variance_linear_ * self.linear_velocity_y_ + self.motion_variance_linear_ * self.kalman_odom_.twist.twist.linear.y) / (self.motion_variance_linear_ + self.measurement_variance_linear_)

     def statePredictionLinear(self, odom_linear_x, odom_linear_y):
          # State prediction for linear velocities
          self.linear_velocity_x_ += odom_linear_x
          self.linear_velocity_y_ += odom_linear_y

     def updateOdometry(self, delta_time):
          # Calculate the change in position
          delta_x = self.linear_velocity_x_ * delta_time
          delta_y = self.linear_velocity_y_ * delta_time

          # Calculate the change in orientation (theta)
          delta_theta = self.mean_angular_z_ * delta_time

          # Update the robot's orientation (theta)
          self.theta_ += delta_theta

          # Update the robot's position (x, y)
          self.x_ += delta_x * math.cos(self.theta_) - delta_y * math.sin(self.theta_)
          self.y_ += delta_x * math.sin(self.theta_) + delta_y * math.cos(self.theta_)

if __name__ == '__main__':
     rospy.init_node('kalman_filter_node')
     filter = KalmanFilter()
     rospy.spin()
