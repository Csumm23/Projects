# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:18:56 2022

@author: chase
"""

#Chase Summerfield
#Program 1
#4/25/2022 10AM


NumberList = []
StringSentence = 0
AverageString = 0
count = 0

String = []

def CountWords(StringSentence):
    global count
    while(count < 10):
        Num = int(input("Enter an integer: "))
    
        while(String.__contains__(Num)):
            Num = int(input("Enter an integer that has not been recorded: "))
    
        String.append(Num)
    
        count += 1
    print("")
    print("---------------------Summary--------------------")
    print("This string is:", String)
    print("The length of this string is: ", len(String))
    print("The sum of this string is: ", (sum(String)))
    AverageString = ((sum(String)) / (len(String)))
    print("The average of this string is: ", AverageString)
    print("------------------------------------------------")
    print("")
CountWords(StringSentence)





#Chase Summerfield
#Program 2
#4/25/2022 10AM


count = 0
StringSentence = 0


def SpaceCheck(StringSentence):
    global count
    
    StringSentence = input("Please enter a sentence: ")
    count += 1
    
    for x in range(len(StringSentence)):
        if StringSentence[x] == " ":
            count += 1
    print("")
    print("There are", count, "words in this sentence.")
    print("")
    print("...........................................")
    print("")

SpaceCheck(StringSentence)






#Chase Summerfield
#Program 3 parts A&B
#4/25/2022 4:30PM



EmployeeID = 0
Salary = 0
BonusPercent = 0
count = 0
BonusAmount = 0
AvgBonusAmount = 0
EmployeeIDs = []
Salaries = []
BonusPercents = []
BonusAmounts = []
TotalBonus = 0
paramSalary = 0
paramBonusPercent = 0

def CalcBonus(paramSalary, paramBonusPercent):
    global EmployeeID, count, TotalBonus, AvgBonusAmount, BonusAmount
    EmployeeID = input("Enter EmployeeID: ")
    
    
    while(EmployeeID != 'quit'):
        
        paramSalary = float(input("Enter salary: "))
        paramBonusPercent = float(input("Enter bonus rate as a decimal: "))
        
        BonusAmount = paramSalary * paramBonusPercent
        count += 1
        
    
        TotalBonus += float(BonusAmount)
        AvgBonusAmount = (TotalBonus / count)
        
        BonusAmounts.append(BonusAmount)
        EmployeeIDs.append(EmployeeID)
        Salaries.append(paramSalary)
        BonusPercents.append(paramBonusPercent)
        
        EmployeeID = input("Enter EmployeeID: ") #Input 'quit' into EmployeeID to kill the loop and report out
        
    Outputs()
    
   
def Outputs():   
    print("")    
    print("=================Summary=================")
    count = 0
    length = len(EmployeeIDs)
    
    while(count < length):
        print("EmployeeID: ", EmployeeIDs[count])
        print("Salary: ", Salaries[count])
        print("Bonus percent: ", BonusPercents[count])
        print("Bonus amount: ", round(BonusAmounts[count], 2))
        print("")
        count += 1
    print("=========================================")
    print("You input values for", count, "employees.")
    print("The total bonus amount was: ", round(TotalBonus, 2))
    print("The average bonus amount was: ", round(AvgBonusAmount, 2))
        
def Main():
    CalcBonus(paramSalary, paramBonusPercent)
Main()