<<<<<<< HEAD
# for element_value in <list,range,set,tuple>:
#     statement


for i in range(1,5):
    print(i)

#for list
list1=["a","b","c"]
for i in list1:
    print(i)

#for tuple
tuple1=("a","b","c")   
for i in tuple1:
    print(i)

#for dict
dict={"n1":"v1","n2":"v2"}
for k in dict:
    print(k)#displays keys


# for k,v in dict:
#     print(k,v)

#to print both key and value
for (k,v) in dict.items():
    print(k,v)

# #else with for and while
# #if loop executes successfully then else block also executed
for value in dict.values():
    print(value)
else:
=======
# for element_value in <list,range,set,tuple>:
#     statement


for i in range(1,5):
    print(i)

#for list
list1=["a","b","c"]
for i in list1:
    print(i)

#for tuple
tuple1=("a","b","c")   
for i in tuple1:
    print(i)

#for dict
dict={"n1":"v1","n2":"v2"}
for k in dict:
    print(k)#displays keys


# for k,v in dict:
#     print(k,v)

#to print both key and value
for (k,v) in dict.items():
    print(k,v)

# #else with for and while
# #if loop executes successfully then else block also executed
for value in dict.values():
    print(value)
else:
>>>>>>> 7324b90fcfd9e427bc3d071c2156a8aaed742496
    print("hi")