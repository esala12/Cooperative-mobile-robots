cmake_minimum_required(VERSION 3.0.2)
project(dreambot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  nav_msgs
  geometry_msgs
  tf
  actionlib
  actionlib_msgs
  visualization_msgs
  message_generation  
)

## Add message files
add_message_files(
  FILES
  PathArray.msg     
  CombinedPathStatus.msg
)

## Add action files
add_action_files(
  DIRECTORY action
  FILES TargetVelocity.action
)


## Generate added messages, services, and actions
generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
  geometry_msgs  # Add dependencies on messages used within your custom messages if necessary
)

## Declare the catkin package
catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS geometry_msgs nav_msgs tf rospy actionlib actionlib_msgs std_msgs visualization_msgs message_runtime
)

## Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Install Python scripts
catkin_install_python(PROGRAMS
  src/fuzzy_wavepoints.py
  src/path_generator.py
  src/wavepoint_generator.py
  src/odom_filter.py
  src/leader_switch.py
  src/create_path.py
  src/fuzzy_leader.py
  src/parameter_publisher.py
  src/reach_goal_client.py
  src/path_service_client.py
  src/path_service_server.py
  src/calculate_args.py
  src/multi_path.py
  src/leader_switch_combine.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
