sumdigit(0,0).
sumdigit(D,S) :-
    M is D mod 10,
    P is D div 10,
    sumdigit(P,X),
    S is M + X.