# def <function_name>(<arguments separated by comma>):
#     statement 1
#     statement 2

#without return
#unparameterised function:
#function definition
def void_function():
    print("hello world")


void_function()#function call

#parametersied function
def void_function(name):
    print("hello ",name)

void_function("sam")

#can have as may parameter as needed
def void_function(name, msg):
    print("hello",name,"msg is",msg)

void_function("sam","Wellcom")

#can be any datatype
def void_function(name ,num):
    print("hello ",name,num)

void_function("sam",[1,2,3])


#with return 
#it can have any datatype 
def add(num1,num2):
    return num1+num2

result=add(1.2,3)
res1=add([1,2],[2,3])
res2=add('ab c'," de")
print(result)
print(res1)
print(res2)

#initialize while defining
#keyWord Arguments
def add(num1=5, num2=0, num3=2):
    return num1 + num2+num3

if __name__ == '__main__':
    result = add(num2=3)
    print(result)


# *args receives tuple
def add_some_numbers(*args):
    print(args)

add_some_numbers(1,2,"str")

#if u want ur function to run according to no.of arguments
def addNum(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)
    # print(args[0]+args[1])

addNum(1,2,3)
addNum(1,2)
addNum(1)



#keyWordArgument
def addKeyWordArgs(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

addKeyWordArgs(num1=2,num2=2)


#both args and kwargs
def addKeyWordArgs(*args,**kwargs):
    print(args)
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

addKeyWordArgs(1,2,num1=2,num2=2)