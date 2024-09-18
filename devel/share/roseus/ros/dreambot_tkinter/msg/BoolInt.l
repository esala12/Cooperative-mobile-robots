;; Auto-generated. Do not edit!


(when (boundp 'dreambot_tkinter::BoolInt)
  (if (not (find-package "DREAMBOT_TKINTER"))
    (make-package "DREAMBOT_TKINTER"))
  (shadow 'BoolInt (find-package "DREAMBOT_TKINTER")))
(unless (find-package "DREAMBOT_TKINTER::BOOLINT")
  (make-package "DREAMBOT_TKINTER::BOOLINT"))

(in-package "ROS")
;;//! \htmlinclude BoolInt.msg.html


(defclass dreambot_tkinter::BoolInt
  :super ros::object
  :slots (_flag _number ))

(defmethod dreambot_tkinter::BoolInt
  (:init
   (&key
    ((:flag __flag) nil)
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _flag __flag)
   (setq _number (round __number))
   self)
  (:flag
   (&optional (__flag :null))
   (if (not (eq __flag :null)) (setq _flag __flag)) _flag)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; bool _flag
    1
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _flag
       (if _flag (write-byte -1 s) (write-byte 0 s))
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _flag
     (setq _flag (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get dreambot_tkinter::BoolInt :md5sum-) "e8892900a4cac102c481821cbfef5b68")
(setf (get dreambot_tkinter::BoolInt :datatype-) "dreambot_tkinter/BoolInt")
(setf (get dreambot_tkinter::BoolInt :definition-)
      "bool flag
int32 number

")



(provide :dreambot_tkinter/BoolInt "e8892900a4cac102c481821cbfef5b68")


