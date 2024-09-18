; Auto-generated. Do not edit!


(cl:in-package dreambot_tkinter-msg)


;//! \htmlinclude BoolInt.msg.html

(cl:defclass <BoolInt> (roslisp-msg-protocol:ros-message)
  ((flag
    :reader flag
    :initarg :flag
    :type cl:boolean
    :initform cl:nil)
   (number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0))
)

(cl:defclass BoolInt (<BoolInt>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BoolInt>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BoolInt)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dreambot_tkinter-msg:<BoolInt> is deprecated: use dreambot_tkinter-msg:BoolInt instead.")))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <BoolInt>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot_tkinter-msg:flag-val is deprecated.  Use dreambot_tkinter-msg:flag instead.")
  (flag m))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <BoolInt>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dreambot_tkinter-msg:number-val is deprecated.  Use dreambot_tkinter-msg:number instead.")
  (number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BoolInt>) ostream)
  "Serializes a message object of type '<BoolInt>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flag) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BoolInt>) istream)
  "Deserializes a message object of type '<BoolInt>"
    (cl:setf (cl:slot-value msg 'flag) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BoolInt>)))
  "Returns string type for a message object of type '<BoolInt>"
  "dreambot_tkinter/BoolInt")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BoolInt)))
  "Returns string type for a message object of type 'BoolInt"
  "dreambot_tkinter/BoolInt")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BoolInt>)))
  "Returns md5sum for a message object of type '<BoolInt>"
  "e8892900a4cac102c481821cbfef5b68")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BoolInt)))
  "Returns md5sum for a message object of type 'BoolInt"
  "e8892900a4cac102c481821cbfef5b68")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BoolInt>)))
  "Returns full string definition for message of type '<BoolInt>"
  (cl:format cl:nil "bool flag~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BoolInt)))
  "Returns full string definition for message of type 'BoolInt"
  (cl:format cl:nil "bool flag~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BoolInt>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BoolInt>))
  "Converts a ROS message object to a list"
  (cl:list 'BoolInt
    (cl:cons ':flag (flag msg))
    (cl:cons ':number (number msg))
))
