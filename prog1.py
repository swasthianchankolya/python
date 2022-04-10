"""
1.Write a python program using functions to find the largest number in an array 
of 10 numbers.
regno:2117053
date:10/04/2022
"""
from array import *
def maxele(arr):
    max=arr[0]
    n=len(arr)
    for i in range(n):
        if(max<arr[i]):
            max=arr[i]
    return max
size=int(input("enter the number of elements:"))
arr=([])
for i in range(0,size):
    value=int(input("enter the element:"))
    arr.append(value)
    
print("array is:",arr)   
print ('Max of the array is ',maxele(arr)) 