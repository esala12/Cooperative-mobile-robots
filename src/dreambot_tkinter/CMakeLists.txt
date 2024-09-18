cmake_minimum_required(VERSION 3.0.2)
project(dreambot_tkinter)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  std_srvs
  message_generation
)

# Specify the directory where your message files are located (msg directory)
add_message_files(
  FILES
  BoolInt.msg
  BoolString.msg
)

# Generate added messages and services
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS std_srvs std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Install Python scripts
catkin_install_python(PROGRAMS
  src/tkinter_ex1.py
  src/tkinter_ex2.py
  src/tkinter_custom_ex1.py
  src/tkinter_custom_ex2.py
  src/tkinter_custom_ex3.py
  src/tkinter_gui_test1.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
