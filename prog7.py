"""
7.Write a python program to read from and write into a text file in python
regno:2117053
date:10/04/2022
"""
#writing into the file
f=open("sample.txt","w")
name=str(input("enter the text:"))
f.write(name)
f.close()

#reading from the file
f=open("sample.txt","r")
t=f.read()
print("\n--------------------------------------")
print(t)
f.close()
