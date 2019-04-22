#process of creating object is called instanciation 

# what is main function
'''
class sample:
    a=12 #class veriable
    global x,y
    x=int(input("Enter the value"))
    y=int(input("input second value "))
    #it is mendatory to pass variable in method as you will not able able to call via object
    def add(z):
        
        print(z)
#        x=10
 #       y=20
        print(x+y)


    def sub(self):
        print(x-y)



obj=sample()

#location of z and obj will be same

print(sample)
print(sample.a) #access datamembers of class with class name
#method to create object of a class is called instantiation
obj=sample()
print(obj)
print(obj.a) #accessing members of class
obj.add()


obj1=sample()
print(obj1)
obj2=sample()
print(obj2)


print(obj1.a)
print(obj2.a)
obj.add()


#num1=int(input("Enter the first Number"))
#num2=int(input("Enter the Second Number"))
obj.add()
obj.sub()

'''

class sample :
    def add (self):
        global num1, num2
        num1=int(input("Enter the value"))
        num2=int(input("Enter the second value"))
        print(num1+num2)

    def sub(m):
        print(num1-num2)

obj=sample()
obj.add()
obj.sub()
print(num1,num2)