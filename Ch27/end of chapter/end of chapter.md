Chapter 27 Exam Style Questions

1.
(a)
BankAccount ---> PersonalAccount
BankAccount ---> SavingsAccount


(b)
```python
class BankAccount(object):
    def __init__(self,n,iban):
        self.AccountHolderName = n;
        self.IBAN = iban;
    def setaccountholdername(self,n):
        self.AccountHolderName = n;
    def getaccountholdername(self):
        return self.AccountHolderName
    def getIBAN(self):
        return self.IBAN
```

(c)
(i)
PersonalAccount
Attributes: MonthlyFee OverdrawLimit
Methods: 
setmonthlyfee() 
setoverdrawlimit() 
getmonthlyfee()
getoverdrawlimit()
pay()
(ii)
SavingsAccount
Attributes: Balance InterestRate
Methods:
setbalance()
getbalance()
setinterestrate()
getinterestrate()
pay()
(iii)
The design is that the class's attributes can be automatically passed into its functions.




2.
a.
SeasonTicketHolder:
TicketHolderEmail: STRING
addNewHolder()
getholdername()
getholderemail()

Pay-As-You-GoTicketHolder:
Account: INTEGER
Price: INTEGER
constructor()
setprice()
getprice()
payfare()
printholderdetails()

ContractTicketHolder:
Account: INTEGER
Fee: INTEGER
setfee()
getfee()
payfee()
printholderdetails()

b.
(i)
Because in that case, attributes can not been modified or called outside the class.
It is easier to debug and ensure data integraty
(ii)
Because functions need to be called outside the class, public methods allows users 
to call functions while they are using.

c.
c = ContractTicketHolder('A. Smith','xyz@abc.xx',10);

3.
a. Containment
b.
```python
class NodeClass(object):
    def __init__(self):
	self.__data = '';
	self.__pointer = -1;
    def setdata(self,d):
	self.__data = d;
    def setpointer(self,p):
	self.__pointer = p;
    def getdata(self):
	return self.__data
    def getpointer(self):
	return self.__pointer
```
c.
```python
class QueueClass(object):
    def __init__(self):
	self.__queue = [NodeClass() for i in range(50)];
	self.__head = -1;
	self.__tail = -1;
```
d.











