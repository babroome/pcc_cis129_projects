# Lab for Module 5 

""" 
Created by Bryce Broome - 3.24.24 

Lab 5 for PCC CIS129 - The Bottle Return Program

Code calculates total number of bottles turned in, and the payout for that number of bottles
"""

# Declare variables

total_bottles = 0 #This variable will store the accumulated bottle values
counter = 1 #This variable will control the loop
today_bottles = 0 #This variable will store the number of bottles returned on a day
total_payout = 0 #This variable will store the calculated value of total_bottles times .10
keep_going = 'y' #This variable will be used to run the program again

# Input loop
while keep_going == 'y':
    while counter <= 7:
        today_bottles = int(input(f'Enter number of bottles for day #{counter}: '))
        total_bottles = total_bottles + today_bottles
        total_payout = total_bottles * .1
        counter += 1
        
# Printing totals
    print('\nThe total number of bottles collected is', total_bottles)
    print('The total paid out is $ {:.1f}\n'.format(total_payout))

# Loop condition
    keep_going = input("Do you want to enter another week's worth of data? \n (Enter y or n): ")
    print()

# Counter/accumulator reset
    total_bottles = 0
    counter = 1
    today_bottles = 0
    total_payout = 0
    

