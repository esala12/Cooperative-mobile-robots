; Auto-generated. Do not edit!


(cl:in-package dreambot_tkinter-msg)


;//! \htmlinclude BoolString.msg.html

(cl:defclass <BoolString> (roslisp-msg-protocol:ros-message)
  ((flag
    :reader flag
    :initarg :flag
    :type cl:boolean
    :initform cl:nil)
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass BoolString (<BoolString>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BoolString>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BoolString)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot_tkinter-msg:<BoolString> is deprecated: use dreambot_tkinter-msg:BoolString instead.")))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <BoolString>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot_tkinter-msg:flag-val is deprecated.  Use dreambot_tkinter-msg:flag instead.")
  (flag m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <BoolString>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot_tkinter-msg:data-val is deprecated.  Use dreambot_tkinter-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BoolString>) ostream)
  "Serializes a message object of type '<BoolString>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flag) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BoolString>) istream)
  "Deserializes a message object of type '<BoolString>"
    (cl:setf (cl:slot-value msg 'flag) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BoolString>)))
  "Returns string type for a message object of type '<BoolString>"
  "dreambot_tkinter/BoolString")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BoolString)))
  "Returns string type for a message object of type 'BoolString"
  "dreambot_tkinter/BoolString")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BoolString>)))
  "Returns md5sum for a message object of type '<BoolString>"
  "887125dffa34591677d9e1a87628fc0c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BoolString)))
  "Returns md5sum for a message object of type 'BoolString"
  "887125dffa34591677d9e1a87628fc0c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BoolString>)))
  "Returns full string definition for message of type '<BoolString>"
  (cl:format cl:nil "bool flag~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BoolString)))
  "Returns full string definition for message of type 'BoolString"
  (cl:format cl:nil "bool flag~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BoolString>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BoolString>))
  "Converts a ROS message object to a list"
  (cl:list 'BoolString
    (cl:cons ':flag (flag msg))
    (cl:cons ':data (data msg))
))
