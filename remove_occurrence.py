# Python Program to Remove the First Occurrence of a Character in a String
'''
string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
string2 = ''
length = len(string)
for i in range(length):
    if(string[i] == char):
        string2 = string[0:i] + string[i + 1:length]
        break

print("Original String :  ", string)
print("Final String :     ", string2)


# Python Program to Remove the First Occurrence of a string in a String

string = input("Please enter your own String : ")
s = input("Please enter your own string of removing : ")
string2 = ''
len_1 = len(string)
len_2 = len(s)
for i in range(len_1):
    if(string[i:i+len_2] == s):
        string2 = string[0:i] + string[i+ len_2 : len_1]
        break
    else:
        string2 = string


print("Original String :  ", string)
print("Final String :     ", string2)
'''
# Python Program to Remove the all Occurrence of a string in a String

string = input("Please enter your own String : ")
s = input("Please enter your own string of removing : ")
string2 = ''
len_1 = len(string)
len_2 = len(s)
while s in string:
    for i in range(len_1):
        if(string[i:i+len_2] == s):
            string2 = string[0:i] + string[i+ len_2 : len_1] #掠過i
            string = string2

print("Final String : ", string)
#string[0]  == I
#string[0: 0] == NONE



        


