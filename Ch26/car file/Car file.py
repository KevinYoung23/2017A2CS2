# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:41:51 2018

@author: Kevin Young
"""
import pickle
class CarRecord:
    def __init__(self,Name,Year,Price, Cylinder):
        self.Name = Name
        self.Year = Year
        self.Price = Price
        self.Cylinder = Cylinder
    def __repr__(self):
        return"(%s,%s,%s,%s)"%(self.Name, self.Year, self.Price, self.Cylinder)
        

ThisCar = CarRecord('', '', 0.00, 0)
Car = [ThisCar for i in range (100)]

Car[1] = CarRecord('VW', '2008', 20000, 4)
Car[2] = CarRecord('Porsche', '2010', 20000000, 8)
Car[3] = CarRecord('BMW', '2009', 370000, 5) 
Car[4] = CarRecord('Mercedes', '2007', 350000, 6)
Car[0] = CarRecord('Audi', '2015', 300000, 6)


def Save():
    file = open('CarFile.DAT', 'rb+')
    for i in range (10):
        pickle.dump(Car[i], file)
    file.close()

def Load():
    file = open('CarFile.DAT', 'rb')
    CarL = []
    for i in range(10): 
        CarL.append(pickle.load(file))
        print (CarL[i])
    file.close()