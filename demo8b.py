
#scope of a variable
value = 1

def increment():
    global value
    value += 1 
    print("incremented value ", value)

def decrement():
    global value
    value -= 1
    print("decremented value", value)

# def method_executor(function_obj):
#     print("within method_executor")
#     print("calling ", function_obj)
#     function_obj()
#     print("calling done")

def add(list2):
    list2.append(3)

def add_kv(dict2):
    dict2["new_key"] = "new_value"

if __name__ == "__main__":
    # list1 = [1,2]
    # print(list1)
    # add(list1)
    # print(list1)
    dict1 = {1 : "value"}
    print(dict1)
    add_kv(dict1)
    print(dict1)
    

    # dynamic_call(decrement)
    # method_executor(increment)
    # method_executor(decrement)
    # print("test variable before foo -", test)
    

    # print("test variable after foo -", test)
    
    # input_list = ["apple"]
    # print(input_list)
    # modify(input_list)
    # print(input_list)

    # input_str = "test"
    # modify_str(input_str)
    # print(input_str)

# def modify(input_list):
#     input_list.append(2)
#     print(input_list)

# def modify_str(input_str):
#     input_str += " append"
#     print(input_str)


