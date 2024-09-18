cmake_minimum_required(VERSION 3.0.2)
project(masterbot_gazebo)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


include_directories(

  ${catkin_INCLUDE_DIRS}
)

