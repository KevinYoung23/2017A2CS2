# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:22:02 2018

@author: Kevin Young
"""
import datetime 
class LibraryItem:
    def  __init__(self, t, a, i): 
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = 0
    
    def gettitle(self):
        return(self.__Title)
    def getauthor_artist(self):
        return(self.__Author_Artist)
    def getitemID(self):
        return(self.__ItemID)
    def getonloan(self):
        return(self.__OnLoan)
    def getduedate(self):
        return(self.__DueDate)
    
    def borrowing(self,i,x):
        if x.getitemonloan() < 5:
            self.__OnLoan = True
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
            self._BorrowerID = x.getborrowerID()
        else:
            print('too many books on loan')
   
    def returning(self,i,x):
        self.__OnLoan = False
        x.updateitemsonloan(-1)
   
    def printdetails(self): 
         print(self.__Title, ' ; ', self.__Author_Artist, end='')       
         print(' ; ', self.__ItemID, ' ; ', self.__OnLoan)       
         print(self.__DueDate, ' ; Borrower: ', self.__BorrowerID) 

class Book(LibraryItem):
    def __init__(self, t, a, i):
         LibraryItem.__init__(self, t, a, i)       
         self.__IsRequested = False 
         self.__RequestedBy = 0
    
    def getIsRequested(self):       
           return(self.__IsRequested) 
     
    def getRequestedBy(self):       
           return(self.__RequestedBy) 
     
    def RequestBook(self, i, x):       
           self.__IsRequested = True       
           self.__RequestedBy = x.getBorrowerID() 
     
    def printDetails(self):       
           LibraryItem.printDetails(self)       
           print(self.__IsRequested, ';', self.__RequestedBy)
            
#    ThisBook.setisrequested(345)
#    ThisBook.printdetails()
        
class CD(LibraryItem):
    def __init__(self, t, a, i):
         LibraryItem.__init__(self, t, a, i)       
         self.__IsRequested = False 
    
    def getgenre(self):       
         return(self.Genre) 
     
    def setisrequested(self, g):       
        self.__genre = g
        
    def printdetails(self):
        print('CD Details')
        LibraryItem.printdetails(self)
        print(self.__Genre)

class Borrower():
    def __init__(self,n,e,b):
         self.__BorrowerName = n       
         self.__EmailAddress = e       
         self.__BorrowerID = b       
         self.__ItemsOnLoan = 0 
         
    def getborrowername(self):
        return (self.__BorrowerName)
    
    def getemailaddress(self):
        return (self.__EmailAddress)
    
    def getborrowerID(self):
        return (self.__BorrowerID)
    
    def getitemsonloan(self):
        return (self.__ItemsOnLoan)
    
    def updateitemsonloan(self, n):
        self.__ItemsOnLoan += n
    
    def printdetails(self) :       
        print("Borrower     : ", self.__BorrowerName)       
        print("ID           : ", self.__BorrowerID)       
        print("email        : ", self.__EmailAddress)       
        print("Items on loan: ", self.__ItemsOnLoan)  
        
        
#display menu**********************************************************
def displaymenu():
     print('1 - Add a new borrower')    
     print('2 - Add a new book')    
     print('3 - Add a new CD')    
     print('4 - Borrow book')    
     print('5 - Return book')    
     print('6 - Borrow CD')    
     print('7 - Return CD')    
     print('8 - Request book')    
     print('9 - Print all details')    
     print('99 - Exit program')    
     print    
     


def main():
    Finish = False
    NextBorrowerID = 1
    NextBookID = 1
    NextCD_ID = 1
    
    while Finish == False:
        displaymenu()
        MenuChoice = int(input('Enter your menu choice: '))
        
        if MenuChoice == 1:
            BName = input("Borrower's name is ")        
            Email = input("Email address: ")         
            BorrowerID = NextBorrowerID          
            NextBorrowerID = NextBorrowerID + 1          
            Bo = Borrower(BName, Email, BorrowerID)  
        elif MenuChoice == 2:
            Title = input("Title: ")          
            Author = input("Author: ")          
            ItemID = NextBookID          
            NextBookID = NextBookID + 1          
            B = Book(Title, Author, ItemID)
        elif MenuChoice == 3:
            Title = input("Title: ")          
            Artist = input("Artist: ")          
            ItemID = NextCD_ID          
            NextCD_ID = NextCD_ID + 1          
            C= CD(Title, Artist, ItemID)
        elif MenuChoice == 4:
            BorrowerID = input("Borrower ID: ")          
            ItemID = input("Book ID: ")          
            B.borrowing(ItemID, Borrower)
        elif MenuChoice == 5:
            BorrowerID = input('Borrower ID: ')
            ItemID = input('Book ID:')
            B.returning(ItemID, Bo)
        elif MenuChoice == 6:
            BorrowerID = input("Borrower ID: ")          
            ItemID = input("CD ID: ")         
            C.borrowing(ItemID, Bo) 
        elif MenuChoice == 7:
            BorrowerID = input("Borrower ID: ")          
            ItemID = input("CD ID: ")          
            C.returning(ItemID, Bo) 
        elif MenuChoice == 8:
            BorrowerID = input("Borrower ID: ")          
            ItemID = input("Book ID: ")          
            C.requestbook(ItemID, Bo)
        elif MenuChoice == 9:
            print("Borrower Details")          
            Borrower.printdetails()          
            print("Book Details")          
            Book.printdetails()          
            print("CD Details")          
            C.printdetails()
        elif MenuChoice == 99:
            Finish == True
        else:
            print('wrong input')
    input()


#def test():    
#    NewBorrower = Borrower("Sylvia", "adc@cie", 123)    
#    NewBorrower.updateitemsonloan(3)    
#    NewBorrower.printdetails()    
#    NewBorrower.updateitemsonloan(-1)    
#    NewBorrower.printdetails()
#    ThisBook = Book("Computing", "Sylvia", 1234)    
#    ThisBook.printdetails()    
#    NewBorrower = Borrower("Fred", "adc@cie", 123)    
#    ThisBook.borrowing(123)    
#    NewBorrower.updateitemsonloan(1)    
#    ThisBook.printdetails()    
#    NewBorrower.printdetails() 
# 
    