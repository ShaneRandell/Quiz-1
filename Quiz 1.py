'''This code will take the following values for the seed number F0 and F1,
and add them using the formula Fn = Fn-1+ fn-2'''

import math 'imported library math


'definig function F(n) where n will be how many numbers you want to print'

def F(n): 
    
    F0,F1 = 0,1  'declairing my seed numbers'
    
    if n == 1:    'and if statement incase the used only wants to print out 1 number in the sequence'
        print(F0)
    
    else:         'else statement for everything other than n==1'
        print(F0)
        print(F1)
    

    for i in range(2,n): 'for loop to run the sequence "n" times, depending on user input'
    'starting at range 2, becasue the first 2 numbers are our seed numbers and will always print'
        
        
        F2 = F0+F1 'this is the additon that will add the variables'
        F0 = F1    'F0 = F1 will swap that place values of the varibles'
        F1 = F2    'F1=F2 will swap the place values of the varibles'
        
        print(F0+F1) 'This will print the newly added place holder values everything the loop starrts ovver'
        
F(10)  'Calling the function to run "n" times that the user wants"