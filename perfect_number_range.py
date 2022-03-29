MinValue = int(input("Enter any Minimum Value:"))
MaxValue = int(input("Enter any Maximum Value:"))

for Number in range(MinValue, MaxValue):
    Sum = 0
    for n in range(1, Number-1):
        if(Number % n == 0):
            Sum = Sum + n
    # display the result
    if(Sum == Number):
        print("%d " %Number)