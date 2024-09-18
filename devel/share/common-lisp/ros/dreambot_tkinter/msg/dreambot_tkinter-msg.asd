
(cl:in-package :asdf)

(defsystem "dreambot_tkinter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BoolInt" :depends-on ("_package_BoolInt"))
    (:file "_package_BoolInt" :depends-on ("_package"))
    (:file "BoolString" :depends-on ("_package_BoolString"))
    (:file "_package_BoolString" :depends-on ("_package"))
  ))