f=open("dbms.txt","w")
t=0
while t<5:
    name="helllo swasthik here im hot"
    f.write(name)
f.close()

f=open("dbms.txt","r")
for t in range(5):
    t1=f.read()
    print(t1)
    t=t+1
f.close()