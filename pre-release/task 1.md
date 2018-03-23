Pre-release 
Task 1


Task 1.1

Research the purpose of JSP structure diagrams.



Taks 1.2

Find out the meaning of the different symbols inside the boxes and how these affect the structure of the program.



Repetition is shown by an asterisk(*) in the corner of components that are repeated.

Selection is shown by a circle in the corner of components where only one is chosen.

These affect the structure of the program by adding loops(while) or boolean expressing(if).





Task 1.3

While
 
    CALL ReadSalary()

    IF Salary>50:

        THEN

           IF Salary>90

              Then

                 Role-Project Manager

              Else

                 Role-Lead Developer

           ENDIF

        ELSE

           Role-Manager

    ENDIF

ENDWHILE



Task 1.4

Add another block that says salary > 70
if False, assign the role as leaddeveloper
if True, goes to the selection of salary >= 90
change that False situation to assign the role as consultant. 

Task 1.5


Change line 5 to IF salary >=70
Change line 6 to IF salary >=90
change the rest of the code like following, 
THEN Role <--- projectmanager
ELSE Role

 <--- consultant
ENDIF
ELSE 
Role <--- leaddeveloper
ELSE
Role <--- manager

Task 1.6

Write a function in program code to determine the role of a staff member.
The function will take salary as its parameter, and return the role.

Look at the python file Task 1.6.py



