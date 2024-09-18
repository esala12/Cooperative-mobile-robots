#!/usr/env/bin python3
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

class KalmanFilter(object):

     def __init__(self):
          self.odom_sum_ = rospy.Subscriber("/slave_odom", Odometry, self.odomCallback)
          self.imu_sub_ = rospy.Subscriber("/slave_robot_imu", Imu, self.imuCallback)
          self.odom_pub_ = rospy.Publisher("/slavebot_kalman", Odometry, queue_size=10)

          self.mean_ = 0.0
          self.variance_ = 1000.0
          self.imu_angular_z_ = 0.0
          self.is_first_odom_ = True
          self.last_angular_z_ = 0.0
          self.motion_ = 0.0
          self.kalman_odom_ = Odometry()
          self.motion_variance_ = 4.0
          self.measurement_variance_ = 0.5

          self.kalman_odom_.header.frame_id = "slave_odom_kalman"
          self.kalman_odom_.child_frame_id = "slave_base_footprint_kalman"

     def imuCallback(self, imu):
          self.imu_angular_z_ = imu.angular_velocity.z

     def odomCallback(self, odom):
          self.kalman_odom_ = odom

          if self.is_first_odom_:
               self.mean_ = odom.twist.twist.angular.z
               self.last_angular_z_ = odom.twist.twist.angular.z
               self.is_first_odom_ = False
               return
          
          self.motion_ = odom.twist.twist.angular.z - self.last_angular_z_
          
          self.statePrediction()
          self.measurementUpdate()

          self.kalman_odom_.twist.twist.angular.z = self.mean_
          self.odom_pub_.publish(self.kalman_odom_)

          self.last_angular_z_ = odom.twist.twist.angular.z

     def measurementUpdate(self):
          self.mean_ = (self.measurement_variance_*self.mean_ + self.variance_*self.imu_angular_z_) / (self.variance_+self.measurement_variance_)
          self.variance_ = (self.variance_*self.measurement_variance_) / (self.variance_+self.measurement_variance_)

     def statePrediction(self):
          self.mean_ = self.mean_ + self.motion_
          self.variance_= self.variance_ + self.motion_variance_

if __name__ == '__main__':
     rospy.init_node('kalman_filter_slave_node')
     filter = KalmanFilter()
     rospy.spin()