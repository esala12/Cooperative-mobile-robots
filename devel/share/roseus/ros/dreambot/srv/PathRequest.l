;; Auto-generated. Do not edit!


(when (boundp 'dreambot::PathRequest)
  (if (not (find-package "DREAMBOT"))
    (make-package "DREAMBOT"))
  (shadow 'PathRequest (find-package "DREAMBOT")))
(unless (find-package "DREAMBOT::PATHREQUEST")
  (make-package "DREAMBOT::PATHREQUEST"))
(unless (find-package "DREAMBOT::PATHREQUESTREQUEST")
  (make-package "DREAMBOT::PATHREQUESTREQUEST"))
(unless (find-package "DREAMBOT::PATHREQUESTRESPONSE")
  (make-package "DREAMBOT::PATHREQUESTRESPONSE"))

(in-package "ROS")





(defclass dreambot::PathRequestRequest
  :super ros::object
  :slots (_path_name ))

(defmethod dreambot::PathRequestRequest
  (:init
   (&key
    ((:path_name __path_name) "")
    )
   (send-super :init)
   (setq _path_name (string __path_name))
   self)
  (:path_name
   (&optional __path_name)
   (if __path_name (setq _path_name __path_name)) _path_name)
  (:serialization-length
   ()
   (+
    ;; string _path_name
    4 (length _path_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _path_name
       (write-long (length _path_name) s) (princ _path_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _path_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _path_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass dreambot::PathRequestResponse
  :super ros::object
  :slots (_success _message ))

(defmethod dreambot::PathRequestResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass dreambot::PathRequest
  :super ros::object
  :slots ())

(setf (get dreambot::PathRequest :md5sum-) "6ecd13868fafba67899de9f7428020dc")
(setf (get dreambot::PathRequest :datatype-) "dreambot/PathRequest")
(setf (get dreambot::PathRequest :request) dreambot::PathRequestRequest)
(setf (get dreambot::PathRequest :response) dreambot::PathRequestResponse)

(defmethod dreambot::PathRequestRequest
  (:response () (instance dreambot::PathRequestResponse :init)))

(setf (get dreambot::PathRequestRequest :md5sum-) "6ecd13868fafba67899de9f7428020dc")
(setf (get dreambot::PathRequestRequest :datatype-) "dreambot/PathRequestRequest")
(setf (get dreambot::PathRequestRequest :definition-)
      "string path_name
---
bool success
string message

")

(setf (get dreambot::PathRequestResponse :md5sum-) "6ecd13868fafba67899de9f7428020dc")
(setf (get dreambot::PathRequestResponse :datatype-) "dreambot/PathRequestResponse")
(setf (get dreambot::PathRequestResponse :definition-)
      "string path_name
---
bool success
string message

")



(provide :dreambot/PathRequest "6ecd13868fafba67899de9f7428020dc")


