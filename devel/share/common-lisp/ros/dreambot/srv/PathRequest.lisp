; Auto-generated. Do not edit!


(cl:in-package dreambot-srv)


;//! \htmlinclude PathRequest-request.msg.html

(cl:defclass <PathRequest-request> (roslisp-msg-protocol:ros-message)
  ((path_name
    :reader path_name
    :initarg :path_name
    :type cl:string
    :initform ""))
)

(cl:defclass PathRequest-request (<PathRequest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PathRequest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PathRequest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-srv:<PathRequest-request> is deprecated: use dreambot-srv:PathRequest-request instead.")))

(cl:ensure-generic-function 'path_name-val :lambda-list '(m))
(cl:defmethod path_name-val ((m <PathRequest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-srv:path_name-val is deprecated.  Use dreambot-srv:path_name instead.")
  (path_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PathRequest-request>) ostream)
  "Serializes a message object of type '<PathRequest-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'path_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'path_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PathRequest-request>) istream)
  "Deserializes a message object of type '<PathRequest-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'path_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'path_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PathRequest-request>)))
  "Returns string type for a service object of type '<PathRequest-request>"
  "dreambot/PathRequestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PathRequest-request)))
  "Returns string type for a service object of type 'PathRequest-request"
  "dreambot/PathRequestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PathRequest-request>)))
  "Returns md5sum for a message object of type '<PathRequest-request>"
  "6ecd13868fafba67899de9f7428020dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PathRequest-request)))
  "Returns md5sum for a message object of type 'PathRequest-request"
  "6ecd13868fafba67899de9f7428020dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PathRequest-request>)))
  "Returns full string definition for message of type '<PathRequest-request>"
  (cl:format cl:nil "string path_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PathRequest-request)))
  "Returns full string definition for message of type 'PathRequest-request"
  (cl:format cl:nil "string path_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PathRequest-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'path_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PathRequest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PathRequest-request
    (cl:cons ':path_name (path_name msg))
))
;//! \htmlinclude PathRequest-response.msg.html

(cl:defclass <PathRequest-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass PathRequest-response (<PathRequest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PathRequest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PathRequest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot-srv:<PathRequest-response> is deprecated: use dreambot-srv:PathRequest-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <PathRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-srv:success-val is deprecated.  Use dreambot-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <PathRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot-srv:message-val is deprecated.  Use dreambot-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PathRequest-response>) ostream)
  "Serializes a message object of type '<PathRequest-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PathRequest-response>) istream)
  "Deserializes a message object of type '<PathRequest-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PathRequest-response>)))
  "Returns string type for a service object of type '<PathRequest-response>"
  "dreambot/PathRequestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PathRequest-response)))
  "Returns string type for a service object of type 'PathRequest-response"
  "dreambot/PathRequestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PathRequest-response>)))
  "Returns md5sum for a message object of type '<PathRequest-response>"
  "6ecd13868fafba67899de9f7428020dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PathRequest-response)))
  "Returns md5sum for a message object of type 'PathRequest-response"
  "6ecd13868fafba67899de9f7428020dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PathRequest-response>)))
  "Returns full string definition for message of type '<PathRequest-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PathRequest-response)))
  "Returns full string definition for message of type 'PathRequest-response"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PathRequest-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PathRequest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PathRequest-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PathRequest)))
  'PathRequest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PathRequest)))
  'PathRequest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PathRequest)))
  "Returns string type for a service object of type '<PathRequest>"
  "dreambot/PathRequest")