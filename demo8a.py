#functions

# def <function_name>(<arguments seperated by comma>):
#     <function line 1>
#     <function line 2>

def void_function(name, message):
    print("hello ", name, message)










# def add(number1, number2):
#     return number1 + number2

def add(number1=5, number2=6):
    return number1 + number2

def add_100_numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    
    # sum = 0
    # for arg in args:
    #     sum += arg
    # print(sum)
    # print(args[0]+args[1])
    # print(kwargs)

if __name__ == '__main__':
    # result = add(1)
    # set1 = {1,2,4}
    # set1.update({2,3,4})
    # print(set1)
    # result = add({1,2,4}, {2,3,4})
    # print(result)
    add_100_numbers(1,2,3, number1=34)
    # add_100_numbers(1,2)
    # add_100_numbers(1)
    # print(add(number2=5)
    # add_100_numbers(number1=10, number2=15)




# def func_with_default_values(number1=5, number2=6):
#     return number1 + number2

# def arbitrary_args(*args, **kwargs):
#     # for arg in args:
#     #     print(arg)
#     for key, value in kwargs.items():
#         print(key, value)
    
# if __name__ == "__main__":
#     #print(void_function())
#     # print(add(1,5))
#     # print(add(6,4))
#     # print(add([1,2,3], [4,5,6]))
#     # print(add({"number1": 2,"number2":5}, {"number3": 56, "number1":5}))
#     #print(func_with_default_values(1, 8))
#     arbitrary_args(number1=5, number2=7, sky="sadfasdf")