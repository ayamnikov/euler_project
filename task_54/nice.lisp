;http://projecteuler.net/thread=54;page=3 AUTHOR kmmbvnr

(define royal-flush
  (match-lambda
   ([(A ?x)(K ?x)(Q ?x)(J ?x)(T ?x)] royal-flush)))

(define two-pairs
  (match-lambda
   ([??- (?x ?-) (?x ?-) ??- (?y ?-) (?y ?-) ??-] (list two-pairs x y))))
