/*facts*/
cat(Marshal).
cat(Blacky).
dog(Jack).
dog(erniu).

/*rules*/
animal (P) :- dog(P)
animal (P) :- cat(P)

enemies(P,Q) :- cat(P), dog(Q)
enemies(Q,P) :- cat(Q), dog(P)