# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:54:33 2022

@author: chase
"""
print("")
print("")
print("Savings Projection")
print("__________________")


Count = 0
Compound = 0
Principle = 0
ReturnRate = 0
InitialCalc = 0
Monthly = 0
Interest = 0
Years = 0

def GetPrinciple():
    global Principle
   
    Principle = float(input("Enter principle amount: "))
    
    MonthlyContribution()
    
def MonthlyContribution():
    global Monthly
    Monthly = float(input("Enter your monthly contribution: "))

def GetRate():
    global ReturnRate
    ReturnRate = float(input("Enter expected rate of return as a decimal: "))
    
    Compound()

def Compound():
    global ReturnRate, Monthly, Priniciple, Years, Compound, Count
    
    Compound = float((Principle + (Monthly*12))*(1 + ReturnRate))
    Years = float(input("How many years will you invest?: "))
    
    while((Years - 1) > Count):
        Count += 1
        Compound = float(((Compound + (Monthly*12)) * (1 + ReturnRate)))
        
    Compound = round(Compound, 2)
    Compound = "{:,}".format(Compound)
    
    print("")
    print("__________________________________________________________________")
    print("")
    print("Your intrest will compound to:", "$",Compound, "after", Years, "years of investing!")
    print("")
    print("__________________________________________________________________")
    
    

def Main():
    GetPrinciple()
    GetRate()
Main()