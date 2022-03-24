n=int(input("enter the number:"))
t=n
s=0
while t>0:
    digit=t%10
    s=s+(digit*digit*digit)
    t//=10
if n==s:
    print("armsstrong")
else:
    print("not armstrong")