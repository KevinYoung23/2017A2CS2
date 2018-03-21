male(john).
male(jack).
female(bill).
male(jim).
male(harvey).
female(marshal).
female(X) : - not(male(X)).



pet(rex).

parent(rex, marshal).
parent(harvey, marshal).
parent(bill, marshal).

sister(harvey, rex).

brother(marshal, bill).

couple(rex, bill, harvey).

married(X, Y): -
	parent(X, Z)
	parent(Y, Z)

triplelove(X, Y, Z): -
	couple()
