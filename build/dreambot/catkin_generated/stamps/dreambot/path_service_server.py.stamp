#!/usr/bin/env python3

import rospy
from dreambot.srv import PathRequest, PathRequestResponse  # Ensure the correct package name

# Global variable to store the selected path
selected_path = None

def handle_path_request(req):
    global selected_path
    rospy.loginfo(f"Received path request with path_name: {req.path_name}")

    # Validate the request and set the selected path
    if req.path_name == "path1":
        selected_path = 1
        response_message = "Path 1 selected."
    elif req.path_name == "path2":
        selected_path = 2
        response_message = "Path 2 selected."
    else:
        rospy.logerr("Invalid path name received.")
        return PathRequestResponse(success=False, message="Invalid path name received.")

    rospy.loginfo(f"Selected path: {selected_path}")
    return PathRequestResponse(success=True, message=response_message)

def path_server():
    rospy.init_node('path_server')
    service = rospy.Service('path_service', PathRequest, handle_path_request)
    rospy.loginfo("Path service server is ready.")
    rospy.spin()    

if __name__ == "__main__":
    path_server()
