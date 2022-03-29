n=int(input("enter the first range:"))
m=int(input("enter the last range:"))
flag=0
for i in range(n,m):
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print(i)