# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:42:10 2022

@author: chase
"""

#Chase Summerfield
#4/11/2022

print("")
print("ICI Looping Sales Program")
print("Created by: Chase Summerfield")

#Initializing variables

State = 0
Date = 0
Count = 0
TaxRate = 0
PreTaxAmount = 0
PostTaxAmount = 0
TotalPreTaxAmount = 0
TotalPostTaxAmount = 0
HighPostTaxAmount = 0
AveragePostTaxAmount = 0
HighSaleID = 0

def GetState():
    global State
    State = input("Enter State: ")                          #Set State Value
    
def GetDate():
    global Date
    Date = input("Enter Date: ")                            #Set Date Value
    
def GetRate():
    global TaxRate, State, Date
    TaxRate = float(input("Enter tax rate as a decimal: ")) #Set TaxRate Value
    print(" ")
    print("____________________")
    print("State: ", State)                                 #Output State
    print("Date: ", Date)                                   #Output Date
    print("Tax Rate: ", TaxRate)                            #Output TaxRate
    print("____________________")
    return TaxRate

def UpdateVals():
     global PreTaxAmount, PostTaxAmount, TotalPreTaxAmount, TotalPostTaxAmount, AveragePostTaxAmount, TaxRate, Count
     
     Count += 1                                          #Update Count
     PostTaxAmount = PreTaxAmount * (1 + TaxRate)        #Define posttax amount
     TotalPreTaxAmount += PreTaxAmount                   #Update TotalPreTaxAmount
     TotalPostTaxAmount += PostTaxAmount                 #UpdateTotalPostTaxAmount
     AveragePostTaxAmount = TotalPostTaxAmount / Count   #Update AveragePostTaxAmount
     
     HighCheck()                                         #Call the highcheck function
     
def HighCheck():
    global PostTaxAmount, HighPostTaxAmount, SaleID, HighSaleID 
    
    if(PostTaxAmount > HighPostTaxAmount):               #Check for the high post tax sale amount   
        HighPostTaxAmount = PostTaxAmount               #If true update HighPostTax
        HighSaleID = SaleID                             #If true update HighSaleID
        return HighSaleID, HighPostTaxAmount
    
def SaleLoop():
#Loop and output SaleID, Pretax amount
#Output post tax amount
    global SaleID
    
    SaleID = input("Enter saleID: ")
    while(SaleID != 'quit'):                            #Loop while SaleID does not evaluate as 'quit'
        global PreTaxAmount, PostTaxAmount
        
        PreTaxAmount = float(input("Enter Pre Tax Amount: "))                                   #Input pretax amount
        
        while(PreTaxAmount > 29999.99):                                                         #$30,000 pretax limit check
            PreTaxAmount = float(input("Please enter pre tax amount lower than $30,000: "))     #Update pretax val to be lower than $30,000
        
        UpdateVals()                                                                            #Call the UpdateVals function
        
        #Output values post update
        print(" ")
        print("Sale Summary:")
        print("______________________________")
        print("SaleID: ", SaleID)           
        print("PreTax Amount: ", round(PreTaxAmount, 2))                            #Print rounded pretax amount
        print("PostTax Amount: ", round(PostTaxAmount, 2))                          #Print rounded post tax amount
        print("______________________________")
        SaleID = input("Enter a new SaleID: ")                                      #Loop and update SaleID
        
def Outputs():
#Total summary sale values
    print(" ")
    print("-----------ICI:Total Daily Summary----------")               #Title
    print("____________________________________________")               #Formatting
    print("State: ", State)                                             #Print State
    print("Date: ", Date)                                               #Print Date
    print("Tax Rate: ", TaxRate)                                        #Print TaxRate
    print("____________________________________________")               #Formatting
    print("Sales: ", Count)                                             #Print Count
    print("Total Pre-Tax Sales Amount: ", round(TotalPreTaxAmount, 2))        #Print rounded total pretax
    print("Total Post-Tax Sales Amount: ", round(TotalPostTaxAmount, 2))      #Print rounded total post tax
    print("Average Post-Tax Sales amount: ", round(AveragePostTaxAmount, 2))  #Print rounded avg post tax
    print("High Post-Tax Sale Amount: ", round(HighPostTaxAmount, 2))        #Print rounded HighPostTaxAmount
    print("High SaleID: ", HighSaleID)                                  #Print HighSaleID
    print("____________________________________________")
    
def Main():
    GetState()
    GetDate()
    GetRate()
    SaleLoop()
    Outputs()
Main()