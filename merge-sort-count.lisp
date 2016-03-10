(defun supermerge (list1 list2 size-list1 &optional (inv 0))
  (cond ((null list1) (values list2 inv))
	((null list2) (values list1 inv))
	((< (car list1) (car list2))
	 (multiple-value-bind (thelist ninv)
	     (supermerge (cdr list1) list2 (- size-list1 1) inv)
	   (values (cons (car list1) thelist) ninv)))
	(t (multiple-value-bind (thelist ninv)
	       (supermerge list1 (cdr list2) size-list1 inv)
	     (values (cons (car list2) thelist) (+ ninv size-list1))))))


(defun merge-sort-count (alist &optional (size -1))
  (let* ((size (if (< size 0)
		   (length alist)
		   size))
	   (half (floor size 2)))
    (if (>= size 2)
	(multiple-value-bind (list1 inv1)
	    (merge-sort-count (subseq alist 0 half) half)
 	  (multiple-value-bind (list2 inv2)
	      (merge-sort-count (subseq alist half) (- size half))
	    (supermerge list1 list2 half (+ (if inv1
						inv1
						0)
					    (if inv2
						inv2
						0)))))
	alist)))

(defun txt2list (name)
  (time (with-open-file (in name)
	  (let ((res))
	    (do ((line (read-line in nil nil)
		       (read-line in nil nil)))
		((null line)
		 (reverse res))
	      (push (parse-integer line) res))))))
