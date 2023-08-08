#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:25:10 2022

CSE 231 PROJECT 5

Algorithm
    Outputs welcome statement and information on what to input
    Prompts user to continue with code or end
    User inputs rental information
    Outputs customer summary
    Calculates payment due based on customer information and outputs
    Prompts user to restart code or end
Closing statement

"""
import math 

#Outputs the welcome message and what the user should input when prompted
print('\nWelcome to Horizons car rentals.')
print('\nAt the prompts, please enter the following: ')
print("\tCustomer's classification code (a character: BD, D, W)")
print('\tNumber of days the vehicle was rented (int)')
print('\tOdometer reading at the start of the rental period (int)')
print('\tOdometer reading at the end of the rental period (int)')

continue_str = input('\nWould you like to continue (A/B)? ') #Asks the user if they would like to continue with the inputting proccess

#while loop that runs as long as the user inputs A
while continue_str == 'A' :
    code_str = input('\nCustomer code (BD, D, W): ') #Asks for classification code
    #while statement that ensures a valid customer code entered
    while code_str != 'BD' and code_str != 'D' and code_str != 'W':
        print("\n\t*** Invalid customer code. Try again. ***")
        code_str = input('\nCustomer code (BD, D, W): ')
    #customer inputs car rental information
    days_str = input('\nNumber of days: ')
    odm_start_str = input('Odometer reading at the start: ')
    odm_end_str = input('Odometer reading at the end:   ')
    odm_start = int(odm_start_str)
    odm_end = int(odm_end_str)
    days_int = int(days_str)
    #Accounts for when the start odm is larger than the end and converts to actual miles
    if odm_end > odm_start :
        miles_int = round((odm_end - odm_start) *0.10,1)
    elif odm_start > odm_end:
        odm = 100000 - ((odm_start - odm_end)*0.1)
        miles_int = round(odm,1)
    #Outputs customer summary
    print("\nCustomer summary:")
    print("\tclassification code:", code_str)
    print("\trental period (days):",days_int)
    print("\todometer reading at start:", odm_start)
    print("\todometer reading at end:  ",odm_end)
    print("\tnumber of miles driven: ", miles_int)
    #decides the correct amount due for each classification code
    if code_str == 'BD' :
        charge_float = round((days_int * 40) + (miles_int * 0.25),2)
        print("\tamount due: $",float(charge_float))
    elif code_str == 'D' :
        miles_per_day = miles_int / days_int
        if miles_per_day <= 100 :
            mileage_charge = 0
        elif miles_per_day > 100 :
            mileage_charge = (miles_int - days_int*100)*0.25
        charge_float = round((60*days_int) + mileage_charge, 2)
        print("\tamount due: $",float(charge_float))
    elif code_str == 'W' :
        weeks_int = math.ceil(days_int / 7)
        miles_per_week = miles_int / weeks_int 
        if miles_per_week <= 900 :
            mileage_charge = 0
        elif 900 < miles_per_week <= 1500 :
            mileage_charge = 100 * weeks_int
        elif miles_per_week > 1500 :
            mileage_charge = (200 * weeks_int) + ((miles_int - (weeks_int*1500))*0.25)
        charge_float = round((190*weeks_int)+mileage_charge,2)
        print("\tamount due: $",float(charge_float))
    #At the end of the loop, prompts to restart or end the loop
    continue_str = input('\nWould you like to continue (A/B)? ')

print('Thank you for your loyalty.') #prints when the user inputs B
