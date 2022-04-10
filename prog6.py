"""
6.Write a Python program to find the largest among 10 numbers stored in a list
regno:2117053
date:10/04/2022
"""
size=int(input("enter the number of elements:"))
list=[]
for i in range(0,size):
    value=int(input("enter the element:"))
    list.append(value)
 
max=list[0]
for j in range(,size):
    if list[0] < list[j]:
        max=list[j]
         
print("original list:",list)
print("largest element:",max)