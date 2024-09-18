execute_process(COMMAND "/home/esala/dreambot_ws/build/dreambot_examples/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/esala/dreambot_ws/build/dreambot_examples/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
