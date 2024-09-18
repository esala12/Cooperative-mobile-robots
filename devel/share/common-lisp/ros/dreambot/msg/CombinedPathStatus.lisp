; Auto-generated. Do not edit!


(cl:in-package dreambot-msg)


;//! \htmlinclude CombinedPathStatus.msg.html

(cl:defclass <CombinedPathStatus> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type dreambot-msg:PathArray
    :initform (cl:make-instance 'dreambot-msg:PathArray))
   (node_active
    :reader node_active
    :initarg :node_active
    :type cl:boolean
    :initform cl:nil)
   (path_published
    :reader path_published
    :initarg :path_published
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CombinedPathStatus (<CombinedPathStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CombinedPathStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CombinedPathStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-msg:<CombinedPathStatus> is deprecated: use dreambot-msg:CombinedPathStatus instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <CombinedPathStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-msg:path-val is deprecated.  Use dreambot-msg:path instead.")
  (path m))

(cl:ensure-generic-function 'node_active-val :lambda-list '(m))
(cl:defmethod node_active-val ((m <CombinedPathStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-msg:node_active-val is deprecated.  Use dreambot-msg:node_active instead.")
  (node_active m))

(cl:ensure-generic-function 'path_published-val :lambda-list '(m))
(cl:defmethod path_published-val ((m <CombinedPathStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-msg:path_published-val is deprecated.  Use dreambot-msg:path_published instead.")
  (path_published m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CombinedPathStatus>) ostream)
  "Serializes a message object of type '<CombinedPathStatus>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'path) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'node_active) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'path_published) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CombinedPathStatus>) istream)
  "Deserializes a message object of type '<CombinedPathStatus>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'path) istream)
    (cl:setf (cl:slot-value msg 'node_active) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'path_published) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CombinedPathStatus>)))
  "Returns string type for a message object of type '<CombinedPathStatus>"
  "dreambot/CombinedPathStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CombinedPathStatus)))
  "Returns string type for a message object of type 'CombinedPathStatus"
  "dreambot/CombinedPathStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CombinedPathStatus>)))
  "Returns md5sum for a message object of type '<CombinedPathStatus>"
  "5fe88b32f7d29dd3ec2430f387f8a6ea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CombinedPathStatus)))
  "Returns md5sum for a message object of type 'CombinedPathStatus"
  "5fe88b32f7d29dd3ec2430f387f8a6ea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CombinedPathStatus>)))
  "Returns full string definition for message of type '<CombinedPathStatus>"
  (cl:format cl:nil "dreambot/PathArray path~%bool node_active~%bool path_published~%~%================================================================================~%MSG: dreambot/PathArray~%float64[] x~%float64[] y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CombinedPathStatus)))
  "Returns full string definition for message of type 'CombinedPathStatus"
  (cl:format cl:nil "dreambot/PathArray path~%bool node_active~%bool path_published~%~%================================================================================~%MSG: dreambot/PathArray~%float64[] x~%float64[] y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CombinedPathStatus>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'path))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CombinedPathStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'CombinedPathStatus
    (cl:cons ':path (path msg))
    (cl:cons ':node_active (node_active msg))
    (cl:cons ':path_published (path_published msg))
))
