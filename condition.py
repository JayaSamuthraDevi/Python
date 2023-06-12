# if <condition>:
#     statement 1
# elif <condition>:
#     statement2
# else:
#     statement3

# can use as many elif needed


# to use logical operators
# *and
# *or
# *not

# relational operators
# * ==
# * !=

# can compare different variables
# doesn't give error

a=5
b=5.0
c=4.0
d="str"
a1={1,2}
b1={1,2}
if a==c:
    print("==")
elif not a!=d:
    print("!=")
elif a1==b1:
    print("==")
else:
    print("!=")


#comprehesion
#(value to return if true) if <condition> else (value to return if false) 
abc=a if a>c else c
print(abc)

