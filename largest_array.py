from array import *
def maxele(arr):
    max=arr[0]
    n=len(arr)
    for i in range(n):
        if(max<arr[i]):
            max=arr[i]
    return max
arr = ar.array('i',[10, 21, 12, 13])
print ('Max of the array is ', MaxofArray(a) ) 