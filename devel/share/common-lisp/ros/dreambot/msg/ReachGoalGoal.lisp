; Auto-generated. Do not edit!


(cl:in-package dreambot-msg)


;//! \htmlinclude ReachGoalGoal.msg.html

(cl:defclass <ReachGoalGoal> (roslisp-msg-protocol:ros-message)
  ((start
    :reader start
    :initarg :start
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ReachGoalGoal (<ReachGoalGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ReachGoalGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ReachGoalGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-msg:<ReachGoalGoal> is deprecated: use dreambot-msg:ReachGoalGoal instead.")))

(cl:ensure-generic-function 'start-val :lambda-list '(m))
(cl:defmethod start-val ((m <ReachGoalGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-msg:start-val is deprecated.  Use dreambot-msg:start instead.")
  (start m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ReachGoalGoal>) ostream)
  "Serializes a message object of type '<ReachGoalGoal>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'start) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ReachGoalGoal>) istream)
  "Deserializes a message object of type '<ReachGoalGoal>"
    (cl:setf (cl:slot-value msg 'start) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ReachGoalGoal>)))
  "Returns string type for a message object of type '<ReachGoalGoal>"
  "dreambot/ReachGoalGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ReachGoalGoal)))
  "Returns string type for a message object of type 'ReachGoalGoal"
  "dreambot/ReachGoalGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ReachGoalGoal>)))
  "Returns md5sum for a message object of type '<ReachGoalGoal>"
  "676aa7bfb3ec2071e814f2368dfd5fb5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ReachGoalGoal)))
  "Returns md5sum for a message object of type 'ReachGoalGoal"
  "676aa7bfb3ec2071e814f2368dfd5fb5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ReachGoalGoal>)))
  "Returns full string definition for message of type '<ReachGoalGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Control.action~%bool start  # Goal - whether to start or stop the controller~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ReachGoalGoal)))
  "Returns full string definition for message of type 'ReachGoalGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Control.action~%bool start  # Goal - whether to start or stop the controller~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ReachGoalGoal>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ReachGoalGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'ReachGoalGoal
    (cl:cons ':start (start msg))
))
