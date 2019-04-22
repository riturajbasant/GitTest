'''
def testnum():
    a=int(input("Enter Number : "))
    if(a<=0):
        print("Please enter valid number")
    elif(a%2==0):
        print("You have entered Even Number")
    else:
        print("You have entered Odd number")

testnum()

#and write a program that prints out all the elements of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(a)):
    if(a[i]<5):
        print(a[i])
    else:
        pass

def num():
    a=int(input("Enter the number"))
    
    c=0
    for i in range(0,a+1):
        c=c+i
        
        

    print(c)
num()

#it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
a = int(input("Enter the value"))
for i in range (2,a):
    if(a%i==0):
        print(i)
    else:
        pass



a = [1, 1, 2, 3, 5, 8, 13]
b = [1,8, 9, 10, 11, 12, 13, 21, 34, 55, 89]

c=[]

for i in range(len(b)):

    if not b[i] in a:
        c.insert(b[i])

print(c)


    
a = [1, 1, 2, 3, 5, 8, 13]
b = [1,8, 9, 10, 11, 12, 13, 21, 34, 55, 89]

for i in a:
    print (i)

 

a = str(input("Enter the string value "))
b=[]
c=[]

for i in a:
    c.append(i)

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print("Values of A are ",c)
print("Values of B are ", b)

if c ==b:
    print("Values are palindrome ")
else:
    print("values are not palindrome")




wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if(wrd==rvs):
    print("this is palindrome")
else:
    print("This is not Palindrome")


#List comprehension

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]

for i in a:
    if (i%2==0):
        b.append(i)
print(b)




a = str(input("Enter the value by A "))
b = str(input("Enter the value by B "))
while a !='quit':
    if(a =='quit'):
        break

        if(len(a)>len(b)):
            print(a, 'has input a great value string')
        else:
'''

import random as r

a = (r.randrange(1,10,1))
count=0
b = 0




while (a!=b ):
    b= int(input("Input Number from 0 to 10 "))
        
    
    if(b>10):
        print("Enter valid number")
        break
    count=count+1

    if a < b:
        print("Enter lower number")
    elif a > b:
        print("Enter Higher number")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")





    
    




    
