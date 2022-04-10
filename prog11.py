"""
11.Write a Python program to define Student Class, create student object, 
and method to display student details
regno:2117053
date:10/04/2022
"""
class student:
    def __init__(self):
        self.name=""
        self.reg=""
        self.cls=""
    def get(self):
        self.name=str(input("enter the student name:"))
        self.reg=int(input("enter the student regno:"))
        self.cls=str(input("enter the student class:"))
    def put(self):
        print("\n")
        print("detail--------------student detail-------------")
        print("student name:",self.name)
        print("student regno:",self.reg)
        print("student class:",self.cls)
        print("------------------------------------")
    
obj=student()
obj.get()
obj.put()