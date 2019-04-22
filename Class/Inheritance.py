#Inheritance is the important feature of oops concept in which we inherit the features of one 
# class to another class. Features may be a value or a functionality which is specified in base class.
#and we want to use this features into child class.


# #Inheritance.
#single Inheritance.
#mulitple Inheritance
#hierarchical inheritance
#Hybrid Inheritance
#Example of Single Inheritance
'''
class a:
    ab=23
    def show(self):
        self.a=10
        print("in class a ")
class b(a):
    def show2(self):
        print(self.a)
        print("In the class B")
        print(self.ab)

obj= b()
obj.show()
obj.show2()
print(obj.ab)

#Multi Level Inheritance with method overwriting
class A:
    def __init__(self):
        #super is used call the parent function which has been created with same name.

        print("InIt Init A")

    def show1(self):
        
        print("in the class 1")
class B(A):
    def __init__(self):
        super().__init__()
        print("InIT the initB")
    def show2(self):
        print("In class 2")
class C(B):
    def __init__(self):
        super().__init__()
        print("Init init C")
    def show3(self):
        print("In class C")

obj = C()
obj.show1()
obj.show2()
obj.show3()



#Multiple Inheritance

class A:
    def show1(self):
        print("In A")
    def sample(self):
        print("Sample of A class")
class B:
    def show2(self):
        print("in B")
    def sample(self):
        print("sample of B class")
class C(B,A):
    def show3(self):
        print("In C")
obj=C()
obj.show1()
obj.show2()
obj.show3()
obj.sample() #It will call the sample of A class as in multiple at time only one class can be called

'''

#Hierarichal Inheritance.

class A:
    def show1(self):
        print("In A")
    def sample(self):
        print("Sample of A class")
class B(A):
    def show2(self):
        print("in B")
    def sample(self):
        print("sample of B class")
class C(A):
    def show3(self):
        print("In C")
obj=C()
obj.show1()
obj_B=B()
obj_B.show2()
obj.show3()
obj.sample()

