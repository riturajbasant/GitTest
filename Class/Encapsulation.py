'''
Encapsulation is an important aspect of Object-oriented programming. It is used to restrict access to methods
and variables. In encapsulation, code and data are wrapped together within a single unit from being 
modified by accident.
Data Abstraction and encapsulation both are often used as synonyms. both are nearly synonym because 
data abstraction is achieved through encapsulation.
Abstraction is used to hide internal details and show only functionalities. 

There are three types of modifiers.
1. public : Data can be used from inside and outside
2. Protected : _ is used to make it protected  : It is like a data will be like public member but they should not be directly
accessed from outside
3. Private : __ used to make it private : can't be seen and accessed from outside


#Private
class sample:
    __a=12
    def __show(self): #(we can also make function private by applying __ and it won't be accessible outside of class)
        __ab=39

        print("In show")
        print(self.__a) #we will always call class veriables from objects within a function
        print(__ab) # if we are defining private method into method then we can't access private member outside of the method


obj= sample()
#print(obj.__a) #can't call private member outside of method
#obj.show() #this won't work incase of private method
obj._sample__show()# to call private method Jugad


#if we want to call private out of the class (Jugad method)

print(obj._sample__a)




class A:
    def __sample(self):
        self.__ab=32
        print("Hello world", self.__ab)

class B(A):
    def example(self):
        self._A__sample()
        print("In example ", self._A__ab)

b=B()
b.example()




class __A:
    def sample(self):
        print("In sample")
class B(__A):
    def example (self):
        print("In example")
c=B()
c.sample()
c.example()
'''
#Protected

class A:
    _ab=34
    def sample(self):
        self._a=25
        print("Hello World", self._a)
class B(A):
    def example(self):
        print("hello in example", self._a)
c=B()
print(c._ab)
c.sample()
c.example()









