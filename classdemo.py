<<<<<<< HEAD
class ClsName:
    var1 = "value1"
    var2 = "value2"

    def func1(self):# python it self sends a argument(object reference) to function
        print("funtion 1")
        print(self.var1,"form function")
    
    def func2(self,x,y):#can have many parameter
        self.x=x# just like this in java
        print("function 2","x=",x,"y=",y)

    #constructor
    def __init__(self):
        print("Its a constructor") 

#create object for class
# can create as many objects u need
#<Obj_name = <class_name>()

obj = ClsName()
print(obj.var1)#calling variable of class  by objname
print(obj.var2)

#calling function
obj.func1()
obj.func2(100,100)

#if need to change variable in class access it using class name
ClsName.var1=10
print(ClsName.var1)




=======
class ClsName:
    var1 = "value1"
    var2 = "value2"

    def func1(self):# python it self sends a argument(object reference) to function
        print("funtion 1")
        print(self.var1,"form function")
    
    def func2(self,x,y):#can have many parameter
        self.x=x# just like this in java
        print("function 2","x=",x,"y=",y)

    #constructor
    def __init__(self):
        print("Its a constructor") 

#create object for class
# can create as many objects u need
#<Obj_name = <class_name>()

obj = ClsName()
print(obj.var1)#calling variable of class  by objname
print(obj.var2)

#calling function
obj.func1()
obj.func2(100,100)

#if need to change variable in class access it using class name
ClsName.var1=10
print(ClsName.var1)




>>>>>>> 7324b90fcfd9e427bc3d071c2156a8aaed742496
