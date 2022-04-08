str="hel llo wo45 6r@@##d"

l=len(str)
v=0
c=0
d=0
s=0
t=0
for i in range(0,l):
    if str[i]>='a' and str[i]<='z':
        if str[i]=='a' or str[i]=='i' or str[i]=='e' or str[i]=='o':
            v=v+1
        else:
            c=c+1
    elif str[i]>='0' and str[i]<='9':
        d=d+1
    elif str[i] in '@#$%^':
        s=s+1
    else:
        t=t+1
        
print(v)
print(c)
print(d)
print(s)
print(t)