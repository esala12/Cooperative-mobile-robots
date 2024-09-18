cmake_minimum_required(VERSION 3.0.2)
project(dreambot_examples)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf2_ros
  geometry_msgs
  message_generation
)

catkin_python_setup()

add_service_files(
  FILES
  AddTwoInts.srv
  GetTransform.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS
  tf2_ros
  geometry_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/tf_examples.py
  src/simple_timer.py
  src/simple_service_server.py
  src/simple_service_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})