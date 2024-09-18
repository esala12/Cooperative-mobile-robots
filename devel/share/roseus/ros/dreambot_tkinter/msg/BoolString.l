;; Auto-generated. Do not edit!


(when (boundp 'dreambot_tkinter::BoolString)
  (if (not (find-package "DREAMBOT_TKINTER"))
    (make-package "DREAMBOT_TKINTER"))
  (shadow 'BoolString (find-package "DREAMBOT_TKINTER")))
(unless (find-package "DREAMBOT_TKINTER::BOOLSTRING")
  (make-package "DREAMBOT_TKINTER::BOOLSTRING"))

(in-package "ROS")
;;//! \htmlinclude BoolString.msg.html


(defclass dreambot_tkinter::BoolString
  :super ros::object
  :slots (_flag _data ))

(defmethod dreambot_tkinter::BoolString
  (:init
   (&key
    ((:flag __flag) nil)
    ((:data __data) "")
    )
   (send-super :init)
   (setq _flag __flag)
   (setq _data (string __data))
   self)
  (:flag
   (&optional (__flag :null))
   (if (not (eq __flag :null)) (setq _flag __flag)) _flag)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; bool _flag
    1
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _flag
       (if _flag (write-byte -1 s) (write-byte 0 s))
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _flag
     (setq _flag (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get dreambot_tkinter::BoolString :md5sum-) "887125dffa34591677d9e1a87628fc0c")
(setf (get dreambot_tkinter::BoolString :datatype-) "dreambot_tkinter/BoolString")
(setf (get dreambot_tkinter::BoolString :definition-)
      "bool flag
string data

")



(provide :dreambot_tkinter/BoolString "887125dffa34591677d9e1a87628fc0c")


