
def inc(a):#method variable or parameter
    a+=1
    print("method variable in inc functio",a)
    if True:
        b="string"
    print("value of b",b)#b is stored in local scope 
    global gval#to modify global variable
    gval=2
    print("GlobalValue",gval)
def dec(a):
    a-=1
    b=10#local variable
    gval=4
    print("GlobalValue in anotherFunction",gval)
    print("method variable in dec function",a,"local variable",b)

#variable b cannot be used outside def function
#print(b)#--NameError: name 'b' is not defined

val=2 #golabal variable
#it can be used anywhere needed
inc(val)
dec(val)
print("Global variable",val)
print(globals())#what all functions available for global variable 
print("file",__file__)#returns file location 


#-----------#
#function is treated as object and will also have reference

def egfunc():
    print("its a function")

def functionDemo(function_obj):
    print("within method")
    print("calling function object",function_obj)
    function_obj()
    print("done")

functionDemo(egfunc)

