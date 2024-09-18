
(cl:in-package :asdf)

(defsystem "dreambot-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PathRequest" :depends-on ("_package_PathRequest"))
    (:file "_package_PathRequest" :depends-on ("_package"))
  ))