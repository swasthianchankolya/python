"""
25.Write a program to check the validity of a password given by the user
The password should satisfy the following criteria
1. contain atleast one letter between ‘a’ and ‘z’
2. contain atleast one number between 0 and 9
3. contain atleast one letter between A-Z
4. contain atleast one character $,#,@
5. Minimum length of password is 6
6. Maximum length of password is 12

regno:2117053
date:10/04/2022
"""
l, u, p, d = 0, 0, 0, 0
password = str(input("enter the password:"))
if (len(password) >=6 and len(password)<=12):
    for i in password:
  
        # counting lowercase alphabets 
        if (i.islower()):
            l=1          
  
        # counting uppercase alphabets
        if (i.isupper()):
            u=1            
  
        # counting digits
        if (i.isdigit()):
            d=1         
  
        # counting the mentioned special characters
        if(i=='#'or i=='$' or i=='@'):
            p=1       
if (l>0 and u>0 and d>0 and p>0):
    print("Valid Password")
else:
    print("Invalid Password")