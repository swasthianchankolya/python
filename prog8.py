"""
8.Write a python program to create two class methods. First method accept a 
string from the user, Second method print the string in upper case.
regno:2117053
date:10/04/2022
"""

class accept:
    def __init__(self):
        self.string=""
    def ac(self):
        self.string=input("enter the name:")
    def pr(self):
        print('name:',self.string.upper())
obj=accept()
obj.ac()
obj.pr()

