(define (over-or-under num1 num2) 
    (cond ((< num1 num2) (print '-1))
          ((> num1 num2) (print '1))
          ((= num1 num2) (print '0)))
)

(define (make-adder num) 
    (define (fun inc)
        (+ num inc))
    fun
)

(define (composed f g) 
    (define (fun x)
        (f (g x)))
    fun
)

(define (repeat f n) 
    (if (< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1))))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (cond((zero? b) a)
    (else (gcd b (modulo a b))))
)
