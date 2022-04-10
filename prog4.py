4.Write Python Program to count the number of characters in a string using 
dictionaries. Display the keys and their values in alphabetical Order. 
"""
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
string=str(input("enter the string:"))
print(char_frequency(sorted(string)))

