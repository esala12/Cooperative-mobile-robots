;; Auto-generated. Do not edit!


(when (boundp 'dreambot::TargetVelocityResult)
  (if (not (find-package "DREAMBOT"))
    (make-package "DREAMBOT"))
  (shadow 'TargetVelocityResult (find-package "DREAMBOT")))
(unless (find-package "DREAMBOT::TARGETVELOCITYRESULT")
  (make-package "DREAMBOT::TARGETVELOCITYRESULT"))

(in-package "ROS")
;;//! \htmlinclude TargetVelocityResult.msg.html


(defclass dreambot::TargetVelocityResult
  :super ros::object
  :slots ())

(defmethod dreambot::TargetVelocityResult
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get dreambot::TargetVelocityResult :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get dreambot::TargetVelocityResult :datatype-) "dreambot/TargetVelocityResult")
(setf (get dreambot::TargetVelocityResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback

")



(provide :dreambot/TargetVelocityResult "d41d8cd98f00b204e9800998ecf8427e")

