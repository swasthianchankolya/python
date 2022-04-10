"""
9.Write Python program to demonstrate Multiple Inheritance. 
regno:2117053
date:10/04/2022
"""
class company:
    def get(self):
        self.c_name=str(input("enter the company name:"))
        self.c_loc=str(input("enter the location:"))
    def put(self):
        print("\n")
        print("----------------details----------------")
        print("company:",self.c_name)
        print("location:",self.c_loc)
        
#creating employee sub class
class employee(company):
    def get(self):
        super().get()
        self.e_name=str(input("enter the employee name:"))
        self.e_id=str(input("enter the employee id:"))
        self.e_sal=str(input("enter the employee salary:"))
    def put(self):
        super().put()
        print("employee:",self.e_name)
        print("employee id:",self.e_id)
        print("employee sal:",self.e_sal)
        print("-------------------------------------------------")

#creating manager sub class
class manager(company):
    def get(self):
        super().get()
        self.m_name=str(input("enter the manager name:"))
        self.m_id=str(input("enter the manager id:"))
        self.m_sal=str(input("enter the manager salary:"))
    def put(self):
        super().put()
        print("manager:",self.m_name)
        print("manager id:",self.m_id)
        print("manager sal:",self.m_sal)
        print("-------------------------------------------------")
e=employee()
m=manager()
print("1.employeee")
print("2.manager")
choice=int(input("enter the choice:"))
if choice==1:
    e.get()
    e.put()
elif choice==2:
    m.get()
    m.put()
else:
    print("invalid choice")