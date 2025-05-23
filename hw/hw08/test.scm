(define (interleave lst1 lst2) 
    (
        cond((null? lst1) lst2)
            ((null? lst2) lst1)
            (else (cons (car lst1) (interleave lst2 (cdr lst1))))
    )
)

(interleave '(1 2 3) '(4 5 6))