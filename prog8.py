"""
Write a python program to create two class methods. First method accept a 
string from the user, Second method print the string in upper case.
"""

class accept:
    def __init__(self):
        self.name=""
        self.regno=""
    def ac(self):
        self.name=input("enter the name:")
        self.regno=input("enter the regno:")
    def pr(self):
        print('name:',self.name.upper())
        print('regno:',self.regno)
obj=accept()
obj.ac()
obj.pr()
