;; Auto-generated. Do not edit!


(when (boundp 'dreambot::TargetVelocityFeedback)
  (if (not (find-package "DREAMBOT"))
    (make-package "DREAMBOT"))
  (shadow 'TargetVelocityFeedback (find-package "DREAMBOT")))
(unless (find-package "DREAMBOT::TARGETVELOCITYFEEDBACK")
  (make-package "DREAMBOT::TARGETVELOCITYFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude TargetVelocityFeedback.msg.html


(defclass dreambot::TargetVelocityFeedback
  :super ros::object
  :slots (_success ))

(defmethod dreambot::TargetVelocityFeedback
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get dreambot::TargetVelocityFeedback :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get dreambot::TargetVelocityFeedback :datatype-) "dreambot/TargetVelocityFeedback")
(setf (get dreambot::TargetVelocityFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
bool success  # Result: indicates if the action was successful


")



(provide :dreambot/TargetVelocityFeedback "358e233cde0c8a8bcfea4ce193f8fc15")


