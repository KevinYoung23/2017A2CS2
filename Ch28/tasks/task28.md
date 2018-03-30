Task 28.01
LDM #2
STO A
LDM #10
STO B
LDD A
ADD B
STO C
LDD B
XOR #&FF
INC ACC B
ADD A
STO D

Task 28.02
LDD A
CMP #0
JPE ELSE
THEN: STO B
JMP ENDIF
ELSE: LDD B
DEC ACC
STO B
ENDIF:......

Task 28.03
LDM #1
STO Number
LDM #0
STO Total
LDM #5
STO Max
LOOP: 
LDD Total
ADD Number
STO Total
LDD Number
INC ACC
STO Number
UNTIL: 
CMP Max
DEC ACC
JPN LOOP
ENDLOOP:

Task 28.04
LDM #0 
STO Count 
LDM #78 
STO Letter 
LOOP: 
LDD Count 
INC ACC 
STO Count 
IN 
CMP Letter       
JPN LOOP 
ENDLOOP

Task 28.05
LDM #0 
STO Count 
LDM #78 
STO Letter 
LOOP: 
LDD Count 
INC ACC 
STO Count 
IN 
CMP Letter       
JPN LOOP 
ENDLOOP:
LDM #48 
ADD Count
OUT        

Task 28.06

| Label | Opcode | Operand |Explanation|
|---|:---:|---:|---:|
||LDD |STACKBASE | |
||STO |STACKPTR  |initialise stack pointer to first location on stack |
|LOOP1:| IN || read character |
|| CMP #13  ||is it the end-of-line character?| 
 ||JPE |LOOP2 |yes ¨C end the loop and go to next loop |
 ||STI| STACKPTR| store character in memory location pointed to by stack pointer |
|| LDD |STACKPTR  ||
||INC |ACC |iIncrement stack pointer |
||STO|STACKPTR|| 
||JMP |LOOP1  ||
|LOOP2:| LDD |STACKPTR || 
 ||CMP|STACKBASE |stack empty ?| 
 ||JPE |ENDWORD  ||
||LDI |STACKPTR |Load contents of memory location at top of stack |
 ||OUT | |output character|
||LDD |STACKPTR  || 
 ||DEC| ACC |decrement stack pointer|
 ||STO |STACKPTR ||
 ||JMP |LOOP2 || 
|ENDWORD: |END||  end of program |
    
    
