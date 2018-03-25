# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:44:31 2018

@author: Kevin Young
"""

# Task 2.3
class Toy():
    def __init__(self, N,I,P,M):
        self.__Name= N
        self.__ID= I
        self.__Price= P
        self.__MinimumAge= M
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
    
# Task 2.4
class ComputerGame(Toy):
    def __init__(self, N,I,P,M,Ca,Co):
        Toy.__init__(self, N,I,P,M)
        self.__Category = Ca
        self.__Console = Co
    def GetCategory(self):
        return(self.__Category)
    def GetConsole(self):
        return(self.__Console)
    
class Vehicle(Toy):
    def __init__(self, N,I,P,M,T,H,L,W):
        Toy.__init__(self, N,I,P,M)
        self.__Type = T
        self.__Height = H
        self.__Length = L
        self.__Weight = W
    def GetType(self):
        return(self.__Type)
    def GetHeight(self):
        return(self.__Height)
    def GetLength(self):
        return(self.__Length)
    def GetWeight(self):
        return(self.__Weight)
    
