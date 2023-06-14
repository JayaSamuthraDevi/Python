<<<<<<< HEAD
#all objects(variables,functions) inherit Object(ObjectClass) 

#syntax
#class ChildClass(ParentClass)

class Calculator:
    name = "calculator"

    def __init__(self,num1,num2):
        self.n1=num1# can create variable --- object scoped  variable 
        self.n2=num2
    
    def add(self):
        self.variable2="some value"
        return self.n1+self.n2

cal_obj =Calculator(2,4)
print(Calculator.name)
print(cal_obj.add())
=======
#all objects(variables,functions) inherit Object(ObjectClass) 

#syntax
#class ChildClass(ParentClass)

class Calculator:
    name = "calculator"

    def __init__(self,num1,num2):
        self.n1=num1# can create variable --- object scoped  variable 
        self.n2=num2
    
    def add(self):
        self.variable2="some value"
        return self.n1+self.n2

cal_obj =Calculator(2,4)
print(Calculator.name)
print(cal_obj.add())
>>>>>>> 7324b90fcfd9e427bc3d071c2156a8aaed742496
print(cal_obj.n1)#n1 is a object scoped variable