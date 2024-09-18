;; Auto-generated. Do not edit!


(when (boundp 'dreambot::CombinedPathStatus)
  (if (not (find-package "DREAMBOT"))
    (make-package "DREAMBOT"))
  (shadow 'CombinedPathStatus (find-package "DREAMBOT")))
(unless (find-package "DREAMBOT::COMBINEDPATHSTATUS")
  (make-package "DREAMBOT::COMBINEDPATHSTATUS"))

(in-package "ROS")
;;//! \htmlinclude CombinedPathStatus.msg.html


(defclass dreambot::CombinedPathStatus
  :super ros::object
  :slots (_path _node_active _path_published ))

(defmethod dreambot::CombinedPathStatus
  (:init
   (&key
    ((:path __path) (instance dreambot::PathArray :init))
    ((:node_active __node_active) nil)
    ((:path_published __path_published) nil)
    )
   (send-super :init)
   (setq _path __path)
   (setq _node_active __node_active)
   (setq _path_published __path_published)
   self)
  (:path
   (&rest __path)
   (if (keywordp (car __path))
       (send* _path __path)
     (progn
       (if __path (setq _path (car __path)))
       _path)))
  (:node_active
   (&optional (__node_active :null))
   (if (not (eq __node_active :null)) (setq _node_active __node_active)) _node_active)
  (:path_published
   (&optional (__path_published :null))
   (if (not (eq __path_published :null)) (setq _path_published __path_published)) _path_published)
  (:serialization-length
   ()
   (+
    ;; dreambot/PathArray _path
    (send _path :serialization-length)
    ;; bool _node_active
    1
    ;; bool _path_published
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; dreambot/PathArray _path
       (send _path :serialize s)
     ;; bool _node_active
       (if _node_active (write-byte -1 s) (write-byte 0 s))
     ;; bool _path_published
       (if _path_published (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; dreambot/PathArray _path
     (send _path :deserialize buf ptr-) (incf ptr- (send _path :serialization-length))
   ;; bool _node_active
     (setq _node_active (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _path_published
     (setq _path_published (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get dreambot::CombinedPathStatus :md5sum-) "5fe88b32f7d29dd3ec2430f387f8a6ea")
(setf (get dreambot::CombinedPathStatus :datatype-) "dreambot/CombinedPathStatus")
(setf (get dreambot::CombinedPathStatus :definition-)
      "dreambot/PathArray path
bool node_active
bool path_published

================================================================================
MSG: dreambot/PathArray
float64[] x
float64[] y

")



(provide :dreambot/CombinedPathStatus "5fe88b32f7d29dd3ec2430f387f8a6ea")


