n=int(input("enter the number:"))
n1=0
n2=1
count=0
if n<=0:
    print("invlaid number")
else:
    while count < n: 
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1