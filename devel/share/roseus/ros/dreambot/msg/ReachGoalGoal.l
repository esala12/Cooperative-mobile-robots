;; Auto-generated. Do not edit!


(when (boundp 'dreambot::ReachGoalGoal)
  (if (not (find-package "DREAMBOT"))
    (make-package "DREAMBOT"))
  (shadow 'ReachGoalGoal (find-package "DREAMBOT")))
(unless (find-package "DREAMBOT::REACHGOALGOAL")
  (make-package "DREAMBOT::REACHGOALGOAL"))

(in-package "ROS")
;;//! \htmlinclude ReachGoalGoal.msg.html


(defclass dreambot::ReachGoalGoal
  :super ros::object
  :slots (_start ))

(defmethod dreambot::ReachGoalGoal
  (:init
   (&key
    ((:start __start) nil)
    )
   (send-super :init)
   (setq _start __start)
   self)
  (:start
   (&optional (__start :null))
   (if (not (eq __start :null)) (setq _start __start)) _start)
  (:serialization-length
   ()
   (+
    ;; bool _start
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _start
       (if _start (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _start
     (setq _start (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get dreambot::ReachGoalGoal :md5sum-) "676aa7bfb3ec2071e814f2368dfd5fb5")
(setf (get dreambot::ReachGoalGoal :datatype-) "dreambot/ReachGoalGoal")
(setf (get dreambot::ReachGoalGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Control.action
bool start  # Goal - whether to start or stop the controller

")



(provide :dreambot/ReachGoalGoal "676aa7bfb3ec2071e814f2368dfd5fb5")

