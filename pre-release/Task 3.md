Task 3.1


character(habib).

anmal(fish).
skill(timetravel).
character_type(habib,explorer).

pet(habib,fish).

has_skill(habib,timetravel).




Task 3.2
onlyapet(X,Y) :- character(X), pet(X,Y), NOT(pet(X,Z)), animal(Y)




Task 3.3
character(kevy).

animal(cat).
skill(slamdunk).
pet(kevy,cat).
character_type(kevy,physicist).
has_skill(kevy,slamdunk).

Task 3.4
True

princess

jim

invisibility

jim

Task 3.5
pet(jim,X).

has_skill(X,fly).

skill(X).

character_type(X,princess),pet(X,Y).