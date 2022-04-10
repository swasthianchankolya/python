"""
12.Write a program to catch a divide by zero exception. Add a finally block too. 
regno:2117053
date:10/04/2022
"""
try:  
    a = int(input("Enter the value of a:"))    
    b = int(input("Enter the value of b:"))    
    c = a/b
    print(c)
except:  
    print("Can't divide with zero")  
finally:
    print("\n---------------------------------------")
    print("we are now outside of exception block")

