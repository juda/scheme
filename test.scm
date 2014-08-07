;;; test without side effect

;;; utilities
(define (filter pred? lst)
  (if (null? lst)
      '()
      (if (pred? (car lst))
          (cons (car lst) (filter pred? (cdr lst)))
          (filter pred? (cdr lst)))))

(define (flatmap func lst)
  (apply append (map func lst)))
      
(define (interval start end)
  (if (= start end)
      '()
      (cons start (interval (+ start 1) end))))

(define (any-of? pred? lst)
  (if (null? lst)
      #f
      (or (pred? (car lst)) (any-of? pred? (cdr lst)))))
(define (none-of? pred? lst)
  (not (any-of? pred? lst)))
(define (all-of? pred? lst)
  (if (null? lst)
      #t
      (and (pred? (car lst)) (all-of? pred? (cdr lst)))))

(define (show obj)
  (display obj)
  (newline))

(define (title obj)
  (newline)
  (show obj))

(show "Test without side effect")

;;; basic operations
(title "basic operations")
(define _1 1)
(define _2 2)
(define (_3) 3)
(show (+ _1 _2 (_3)))   ;;6
(show (- _2 (_3)))  ;;-1
(show (* _2 (_3)))      ;;6
(show (/ _2 (_3)))      ;;2/3
(show (quotient _2 (_3)))  ;; 0
(show (modulo _2 (_3)))  ;; 2
(show (if (= _1 1)
             (_3)
             _2))    ;;3

;;; try some big numbers
(title "big numbers")
(define _4 12345678901234567890)
(define _5 98765432109876543210)
(show (* (- _4 _5) (+ _4 200 _5)))  ;; -9602194792318244175459533629632373116000

;;; fast-exp
(title "fast-exp")
(define (sqr x) (* x x))
(define (my-odd? n) (= (modulo n 2) 1))

(define (fast-exp a n)
  (if (= n 0)
      1
      (if (my-odd? n)
          (* a (sqr (fast-exp a (quotient n 2))))
          (sqr (fast-exp a (quotient n 2))))))

(show (fast-exp 2 0)) ;; 1
(show (fast-exp 2 5)) ;; 32
(show (fast-exp 2 100)) ;; 1267650600228229401496703205376

;;; fibonacci
(title "fibonacci sequence")
(define fib
  (lambda (n)
    (letrec ((calc-fib (lambda (prev now n)
                         (if (= n 0)
                             prev
                             (calc-fib now (+ prev now) (- n 1))))))
      (calc-fib 0 1 n))))

(show (fib 5))  ;; 5
(show (fib 20)) ;; 6765
(show (fib 32))  ;; 2178309, test how good your memory management is
;; (define unused_var (fib 50000)) ;; test this if you have implemented tail call optimization

;;; the computeE
(title "compute e")
(define (computeE e k f m)
  (if (> k m)
      e
      (computeE (+ e (/ 1.0 f)) (+ k 1) (* f k) m)))

(show (computeE 0 1 1 100))  ;; 2.7182818##

;;; predicates
(title "predicate eqv?")
(show (and
       (eqv? 'a 'a)
       (not (eqv? 'a 'b))
       (eqv? 'lowercase 'LOwERcaSE)
       (eqv? '() '())
       (eqv? 10000000000000 10000000000000)
       (not (eqv? (cons 1 2) (cons 1 2)))
       (let ((lst (cons 1 2)))
         (eqv? lst lst))
       (not (eqv? (lambda() 1) (lambda () 2)))
       (not (eqv? #f 'nil))
       (let ((p (lambda (x) x)))
        (eqv? p p)))) ;; #t

(title "predicate eq?")
(define (compare-eq?-eqv? x y) (eq? (eq? x y) (eqv? x y)))
(show (and
       (eq? #t #t)
       (eq? #f #f)
       (compare-eq?-eqv? 'a 'a)
       (compare-eq?-eqv? 'a 'b)
       (compare-eq?-eqv? 'lowercase 'LOwERcaSE)
       (compare-eq?-eqv? '() '())
       (compare-eq?-eqv? (cons 1 2) (cons 1 2))
       (let ((lst (cons 1 2)))
         (compare-eq?-eqv? lst lst))
       (compare-eq?-eqv? (lambda () 1) (lambda () 2))
       (compare-eq?-eqv? #f 'nil)
       (let ((p (lambda (x) x)))
         (compare-eq?-eqv? p p)))) ;; #t

(title "predicate equal?")
(define (compare-equal?-eqv? x y)
  (if (eqv? x y)
      (equal? x y)
      #t))
(show (and
       (eq? #t #t)
       (eq? #f #f)
       (compare-equal?-eqv? 'a 'a)
       (compare-equal?-eqv? 'a 'b)
       (compare-equal?-eqv? 'lowercase 'LOwERcaSE)
       (compare-equal?-eqv? '() '())
       (compare-equal?-eqv? (cons 1 2) (cons 1 2))
       (let ((lst (cons 1 2)))
         (compare-equal?-eqv? lst lst))
       (compare-equal?-eqv? (lambda () 1) (lambda () 2))
       (compare-equal?-eqv? #f 'nil)
       (let ((p (lambda (x) x)))
         (compare-equal?-eqv? p p))
       (equal? 'a 'a)
       (equal? '(a) '(a))
       (equal? '(a (b) c) '(a (b) c))
       (equal? "abc" "abc")
       (equal? 2 2))) ;; #t

;;; pairs and lists
(title "pairs and lists")
(show
 (and (equal? '(1 2 3 4) (list 1 2 3 4))
      (equal? (list 1 2 3 4) (cons 1 (cons 2 (cons 3 (cons 4 '())))))
      (equal? (cons 1 (cons 2 (cons 3 (cons 4 '())))) '(1 2 3 4))
      (not (pair? '()))
      (list? '())
      (pair? (cons 1 2))
      (not (list? (cons 1 2)))
      (pair? '(1 2))
      (list? '(1 2))))  ;; #t


(define lst '(1.1 1 2 #\c))
(show (eqv? (cadr lst) 1))  ;; #t
(show (eqv? (list-ref lst (- (length lst) 1)) #\c))  ;; #t
(show (memq 2 lst))  ;; (2 #\c)
(show (memq 100 lst)) ;; #f

(let ((table '((apple 0)
              (banana 1)
              (strawberry 2))))
  (show (assq 'banana table))
  (show (assq 'pineapple table))) 
;; (banana 1)
;; #f

(define (hanoi src dest mid n)
  (if (= n 0)
      '()
      (append (hanoi src mid dest (- n 1))
              (list (list src dest))
              (hanoi mid dest src (- n 1)))))

(show (hanoi 'a 'b 'c 3))  ;; ((a b) (a c) (b c) (a b) (c a) (c b) (a b))

;;; infinite stream
(title "infinite stream")
(define (make-stream start step)
  (cons start (lambda () (make-stream (+ start step) step))))
(define (head stream) (car stream))
(define apply2 (lambda (f) (f)))
(define (tail stream) (apply2 (cdr stream) ))
(define (nth-from stream n)
  (if (= n 0)
      stream
      (nth-from (tail stream) (- n 1))))

(define stream (make-stream 0 1))
(show (head stream))  ;; 0
(show (head (nth-from stream 4))) ;; 4
(define stream (nth-from stream 100))
(show (head stream)) ;; 100

(define (stream-map func . streams)
  (cons (apply func (map head streams)) 
        (lambda () 
          (apply stream-map (append (list func) (map tail streams))))))
(define (minus a b) (- a b))
(define sqrn-minus-n 
  (stream-map minus (stream-map sqr (make-stream 0 1)) (make-stream 0 1)))
(show (head (nth-from sqrn-minus-n 5))) ;; 20
(show (head (nth-from sqrn-minus-n 100))) ;; 9900


;;; N-queens
(title "N-queens")
(define (NQU size)
  (define all-cols (interval 1 (+ size 1)))
  (define (valid? n configuration)
    (and (none-of? (lambda (col) (= (car configuration) col)) (cdr configuration))
         (none-of? (lambda (diag) (= (- n (car configuration)) diag))
                   (map - (interval (+ n 1) (+ size 1)) (cdr configuration)))
         (none-of? (lambda (cdiag) (= (+ n (car configuration)) cdiag))
                   (map + (interval (+ n 1) (+ size 1)) (cdr configuration)))))
  
  (define (choose-col n)
    (if (= n (+ size 1))
        (list '())
        (filter
         (lambda (configuration) (valid? n configuration))
         (flatmap
          (lambda (configuration)
            (map (lambda (sel) (cons sel configuration))
                 all-cols))
          (choose-col (+ n 1))))))
  (choose-col 1))
        
(show (length (NQU 6))) ;; 92

;;; let-bindings
(title "let-bindins")
(define var1 1)
(show (let ((var1 2)
               (y (lambda () var1)))
           (y)))  ;; 1
(show (let* ((var1 2)
                (y (lambda () var1)))
           (y)))  ;; 2
(show (letrec ((var1 2)
                  (y (lambda () var1)))
           (y)))  ;; 2
(show (let* ((var1 2)
             (y var1))
           y))  ;; 2

;;; closure
(title "closure")
(define (make-balance init)  

  (define (reset balance transaction-log k)
    (if (or (null? transaction-log) (<= k 0))
        (list balance transaction-log)
        (cond ((eq? (caar transaction-log) 'add) (reset (- balance (cadar transaction-log)) (cdr transaction-log) (- k 1)))
              ((eq? (caar transaction-log) 'clear) (reset (cadar transaction-log) (cdr transaction-log) (- k 1)))
              ((eq? (caar transaction-log) 'revert) (reset (redo balance (cdr transaction-log) (cadar transaction-log)) (cdr transaction-log) (- k 1))))))
  (define (redo balance transaction-log k)
    (if (or (null? transaction-log) (<= k 0))
        balance
        (cond ((eq? (caar transaction-log) 'add) (redo (+ balance (cadar transaction-log)) (cdr transaction-log) (- k 1)))
              ((eq? (caar transaction-log) 'clear) (redo 0 (cdr transaction-log) (- k 1)))
              ((eq? (caar transaction-log) 'revert) (redo (car (reset balance (cdr transaction-log) (cadar transaction-log))) (cdr transaction-log) (- k 1))))))
  (define (revert balance transaction-log k)
    (car (reset balance transaction-log k)))
  (define (make-balance-impl balance transaction-log)
    (lambda (action . args)
      (cond
        ((eq? action 'get-balance) balance)
        ((eq? action 'get-log) (reverse transaction-log))
        ((eq? action 'add) (make-balance-impl (+ balance (car args)) (cons (cons 'add args) transaction-log)))
        ((eq? action 'clear) (make-balance-impl 0 (cons (list 'clear balance) transaction-log)))
        ((eq? action 'revert) (make-balance-impl (revert balance transaction-log (car args)) (cons (cons action args) transaction-log)))
        ((eq? action 'reset) (apply make-balance-impl (reset balance transaction-log (car args))))
        
        (else (display "unknown action ") (display (cons action args))(newline)))))

  (make-balance-impl init '()))

(define show-balance-details
  (lambda (balance)
    (display "Balance = ")
    (display (balance 'get-balance))
    (newline)
    (display "Transaction log: ")
    (display (balance 'get-log))
    (newline)))

(define account (make-balance 100))
(show-balance-details account)
(define account (account 'add 100))
(show-balance-details account)
(define account (account 'add -20))
(define account (account 'add 5))
(show-balance-details account)
(define account (account 'clear))
(show-balance-details account)
(account 'miaow~~~~ 555 555 "-_-||")
(show-balance-details account)
(define account (account 'revert 1))
(show-balance-details account)
(define account (account 'revert 1))
(show-balance-details account)
(define account (account 'revert 2))
(show-balance-details account)
(define account (account 'reset 5))
(show-balance-details account)

;; Balance = 100
;; Transaction log: ()
;; Balance = 200
;; Transaction log: ((add 100))
;; Balance = 185
;; Transaction log: ((add 100) (add -20) (add 5))
;; Balance = 0
;; Transaction log: ((add 100) (add -20) (add 5) (clear 185))
;; unknown action (miaow~~~~ 555 555 -_-||)
;; Balance = 0
;; Transaction log: ((add 100) (add -20) (add 5) (clear 185))
;; Balance = 185
;; Transaction log: ((add 100) (add -20) (add 5) (clear 185) (revert 1))
;; Balance = 0
;; Transaction log: ((add 100) (add -20) (add 5) (clear 185) (revert 1) (revert 1))
;; Balance = 0
;; Transaction log: ((add 100) (add -20) (add 5) (clear 185) (revert 1) (revert 1) (revert 2))
;; Balance = 180
;; Transaction log: ((add 100) (add -20))