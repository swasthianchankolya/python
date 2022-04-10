"""
2.Write a python program to sort numbers in a list in ascending order using 
bubble sort by passing list as an argument to the function call
regno:2117053
date:10/04/2022
"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                temp=arr[j]
                arr[j]=arr[j + 1]
                arr[j + 1]=temp
 

arr=[]
size=int(input("enter the number of elements:"))
for i in range(0,size):
    value=int(input("enter the element:"))
    arr.append(value)
print("orignal array is:",arr)   

bubbleSort(arr)
 
print ("Sorted array is:")
print(arr)