; Auto-generated. Do not edit!


(cl:in-package dreambot-msg)


;//! \htmlinclude ReachGoalResult.msg.html

(cl:defclass <ReachGoalResult> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ReachGoalResult (<ReachGoalResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ReachGoalResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ReachGoalResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-msg:<ReachGoalResult> is deprecated: use dreambot-msg:ReachGoalResult instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ReachGoalResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-msg:success-val is deprecated.  Use dreambot-msg:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ReachGoalResult>) ostream)
  "Serializes a message object of type '<ReachGoalResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ReachGoalResult>) istream)
  "Deserializes a message object of type '<ReachGoalResult>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ReachGoalResult>)))
  "Returns string type for a message object of type '<ReachGoalResult>"
  "dreambot/ReachGoalResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ReachGoalResult)))
  "Returns string type for a message object of type 'ReachGoalResult"
  "dreambot/ReachGoalResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ReachGoalResult>)))
  "Returns md5sum for a message object of type '<ReachGoalResult>"
  "358e233cde0c8a8bcfea4ce193f8fc15")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ReachGoalResult)))
  "Returns md5sum for a message object of type 'ReachGoalResult"
  "358e233cde0c8a8bcfea4ce193f8fc15")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ReachGoalResult>)))
  "Returns full string definition for message of type '<ReachGoalResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool success  # Result - whether the action completed successfully~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ReachGoalResult)))
  "Returns full string definition for message of type 'ReachGoalResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool success  # Result - whether the action completed successfully~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ReachGoalResult>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ReachGoalResult>))
  "Converts a ROS message object to a list"
  (cl:list 'ReachGoalResult
    (cl:cons ':success (success msg))
))
