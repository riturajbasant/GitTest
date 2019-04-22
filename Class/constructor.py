#contructor : contructor is a special type of method which is automatically  executed when we create an object of the class
#or instantiate a class.

'''
class sample:


    def __init__(x):
        print("This is automatic excution")
#New is a contructor which will be executed without generating reference number
    def __new__(self):
        print("it will be exuted before init")
        print(self)

#if we use the same contructor same twice first will be overwritten by the second constructor
class sample():

    def __init__(self):
        print(self)
        print("It is automatically executed")

    def __init__(self):
        print(self)
        print("it is automatically executed for the last CC")

    def __init__(self, x , y):
        print(x,y)

sample(10,13)

class sample:

    ab= 45843958
    def __init__(a,x,y):
        a.x=x
        a.y=y
        print(a.ab)

    def add(d):
        print("sum is", d.x + d.y)
        print(d.ab)
    
    def sub(self):
        print("sub is ", self.x - self.y)

num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second number : "))
obj=sample(num1,num2)
obj.add()
obj.sub()

'''
#Operator Overload

class Sample:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(one, two):
        x = one.x + one.y
        y = two.y + two.x
        print(x,y)

obj1= Sample(12,13)
obj2 = Sample(45,67)
obj1+obj2
#this is used to check all the special methods
print(dir(obj1))
