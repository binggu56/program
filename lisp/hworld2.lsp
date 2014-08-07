(Defun hello (name &key (from "the world")) 
   (format t "hello ~a from ~a" name from))
   
(hello "jim")

;; (print "hello world")
