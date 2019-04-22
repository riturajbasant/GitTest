#PolyMorphism : poly == many morph == forms

#Two type of polymorphism : 1. methodoverloading 2. methodoverwritting

#Python only support methonoverwritting

class sample:
    a = int(input("Enter Choice"))
    if(a==1):
        def show(self):
            print("In 1 st show")
    else:
        def show(self):
            print("In 2nd show")

obj = sample()
obj.show()

#1. Method overwritting
#2. Method Overloading (Python dont support)
#3. Operator Overloading

class Operator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(one, two):
        x=one.a +two.a
        y= one.b + two.b
        print(x,y)

obj1=Operator(12,13)
obj2=Operator(32,34)
obj1+obj2