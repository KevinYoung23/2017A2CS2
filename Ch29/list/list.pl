len([],0).
len([_|T],L) :-
    len(T,X),
    L is X + 1.

mymember(I,[I|_]).
mymember(I,[_|T]) :-
    mymember(I,T).

lastitem(X,[X]).
lastitem(X,[_|T]) :-
    lastitem(X,T).

myappend([],X,X).
myappend([H|T],M,[H|R]) :-
    myappend(T,M,R).

lastsecond(X,[X,_]).
lastsecond(X,[_|T]) :-
    lastsecond(X,T).

kelement(X,[X|_],1).
kelement(X,[_|T],N) :-
    M is N - 1,
    kelement(X,T,M).

reverselist([],[]).
reverselist([H|T],A|H :-
    reverselist(T,A).

palindrome([],X,X).
palindrome([H|T],L,A) :-
    palindrome(T,L,[H|A]).

