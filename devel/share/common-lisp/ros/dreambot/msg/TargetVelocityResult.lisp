; Auto-generated. Do not edit!


(cl:in-package dreambot-msg)


;//! \htmlinclude TargetVelocityResult.msg.html

(cl:defclass <TargetVelocityResult> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass TargetVelocityResult (<TargetVelocityResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TargetVelocityResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TargetVelocityResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-msg:<TargetVelocityResult> is deprecated: use dreambot-msg:TargetVelocityResult instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TargetVelocityResult>) ostream)
  "Serializes a message object of type '<TargetVelocityResult>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TargetVelocityResult>) istream)
  "Deserializes a message object of type '<TargetVelocityResult>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TargetVelocityResult>)))
  "Returns string type for a message object of type '<TargetVelocityResult>"
  "dreambot/TargetVelocityResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TargetVelocityResult)))
  "Returns string type for a message object of type 'TargetVelocityResult"
  "dreambot/TargetVelocityResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TargetVelocityResult>)))
  "Returns md5sum for a message object of type '<TargetVelocityResult>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TargetVelocityResult)))
  "Returns md5sum for a message object of type 'TargetVelocityResult"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TargetVelocityResult>)))
  "Returns full string definition for message of type '<TargetVelocityResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TargetVelocityResult)))
  "Returns full string definition for message of type 'TargetVelocityResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TargetVelocityResult>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TargetVelocityResult>))
  "Converts a ROS message object to a list"
  (cl:list 'TargetVelocityResult
))
