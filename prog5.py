"""
5.Write Python Program to count the number of times an item appears in the 
list.
regno:2117053
date:10/04/2022
"""
count=0
flag=0

list=[]
size=int(input("enter the number of elements:"))
for i in range(0,size):
    value=int(input("enter the element:"))
    list.append(value)
print("orignal list is:",list)   
search=int(input("enter the element to search:"))
for i in range(0,size):
    if search == list[i]:
        count=count+1
        flag=1
if(flag==0):
    print("number not found")
else:
    print(search,"found",count,"times")
