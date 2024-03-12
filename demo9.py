# class SomeClassName:
#     var1 = "value1"
#     var2 = "value2"

#     def __init__(self, var1, var2):
#         print("im inside constructor")
#         self.var1 = var1
#         self.var2 = var2

#     def function(self):
#         print(self.var1)
    
#     def function2(self):
#         print("function 2")

# if __name__ == "__main__":
#     some_obj = SomeClassName(123123,12312312)
#     some_obj.function()
#     some_obj2 = SomeClassName(123.00,"sdfsdf")
#     some_obj2.function()
#     some_obj.function()
    
    # some_obj.var1 = "new value"
    # print(some_obj.var1)
    
    # some_obj2 = SomeClassName()
    # print(some_obj2.var1)



















class Calculator (object):
    name = "calculator"

    def __init__(self, number1, number2):
        self.n1 = number1
        self.n2 = number2

    def add(self):
        self.variable2 = "some value"
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2        

class ParentClass:
    n1 = 1
    n2 = 2
    def __init__(self):
        print("parent constructor")

class ChildClass(ParentClass):
    def __init__(self):
        print("child constructor")
    def print_n1(self):
        print(self.n1)

if __name__ == "__main__":
    # cal_obj = Calculator(3,5)
    # print(cal_obj.n1)
    child_obj = ChildClass()
    print(child_obj.n1)
    print()
    # print(Calculator.name)
    # print(cal_obj.another_object_scoped_variable)
    # print(cal_obj.add())
    # print(cal_obj.another_object_scoped_variable)
    # print(dir(cal_obj))
    # print(dir(1))