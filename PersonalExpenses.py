# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:00:22 2022

@author: chase
"""

Income = 0
Mortgage = 0
Personal = 0
Savings = 0

def Income():
    global Income
    Income = float(input("Enter annual gross income:"))
    
    if(0 < Income < 9700):
        Income = Income * 0.9
    
    elif(9700 < Income < 39475):
        Income = Income * 0.88
    
    elif(39475 < Income < 84200):
        Income = Income * 0.78
        
    elif(84200 < Income < 160725):
        Income = Income * 0.76
    
    elif(160725 < Income < 204100):
        Income = Income * 0.68
    
    elif(204100 < Income < 510300):
        Income = Income * 0.65
    else:
        Income = Income * 0.63
    
    
    MortgagePayment()
    
    
def MortgagePayment():
    global Income, Mortgage
    
    print("")
    print("____________________________________________________________________")
    print("Estimated annual net income: $", Income)
    
    Mortgage = (Income * 0.34)
    print("")
    print("You can afford a monthly mortgage payment of:", "$", round((Mortgage/12), 2))
    
    Personal()

def Personal():
    global Income, Personal
    Personal = float(Income * 0.11)
    print("")
    print("You can afford:", "$", round((Personal/12), 2), "per month for groceries.")
    print("")
    print("Estimated vheicle cost:", "$", round((Income * 0.07)/12, 2), "per month.")
    print("")
    print("Annual insurance cost estimate:", "$", Income * 0.1)
    print("")
    print("Annual emergency fund cost:", "$", round((Income * 0.07), 2))
    print("")
    print("Remaining funds:", "$", round((Income * 0.31), 2))
    print("")
    print("____________________________________________________________________")
    
    Saving()
    
    
def Saving():
    global Income
    
    print("")
    print("If you invest 10% of your net income you will save:", "$", round(Income * 0.1, 2), "per year.")
    print("You will spend:", "$", round((Income * 0.9), 2), "per year.")
    print(".")
    print("If you invest 20% of your net income you will save:", "$", round(Income * 0.2, 2), "per year!")
    print("You will spend:", "$", round((Income * 0.8), 2), "per year.")
    print(".")
    print("If you invest 30% of your net income you will save:", "$", round(Income * 0.3, 2), "per year!!!")
    print("You will spend:", "$", round((Income * 0.7), 2), "per year.")
    print(".")

def Main():
    Income()
    
Main()