num=10
print(num)
print(type(num))#to get datatype of variable
print(dir(num))#what r the methods can be used with this variable
print(num.numerator)

#variable_name=string --not datatype
####\
##string is immutable
##it modifes the old string and store it in new object old remains same


string="Str"
print(string)
str1='string'
print(str1)
str2="""string
is
string"""
print(str2)
str3='''
string  
is the
string
string'''
print(str3)
print(type(string))
print(dir(string))
str=string.join("some")#treating it(some) as char array and joins value with all element in array
print(str)


#Boolean
#1st letter in capital

var=True
print(var)
print(False)
print(type(var))
print(dir(var))

#List
#mutable,allows multiple datatypes

list=[2,"as",1.0,[2,3,"abc"]]
print(list)
print(list.index(1.0))#treats 1==1.0
print(list.pop())#delets last element
print(dir(list))
print(list.sort())#comapretor faecs issue if different datatypes are there

#add two list
list1=[1,2]
list2=[3,4]
print(list1+list2)

#list of dict
stu=[{"name":"a","age":12},{"name":"b","age":18}]

#Tuple
#immutable

tuple=(1,2,"abc",True)
print(tuple)
print(type((1,"",None)))
print(dir(tuple))


#Set
# dont takes duplicate element and 
#prints in sorted way
#if data type is diffrence it has its own logic and sort doesn't say error

set={1,2,3,"a",7,5,2}
print(set)
print(type(set))
print(dir(set))

set1={"a","c","b"}#alphabets wont sort 
print(set1)

#to sort alphabets
set2=sorted(set1)
print(set2)

#adding set
set1={1,2,3}
set1.update({4,5})
print(set1)


#Range
#(start,end-1,step_value)

#print(range(6))#doesn't print's range values since its a funtion
# print(range(3,6))
# print(range(1,10,2))

#use loop to print range values
for(a in range):
    print(a)


#Dictionary
# ordered*, changeable and do not allow duplicates.
dict={'name1':'abc','name2':'xyz'}
dict1={}
print(dict)
print(type(dict))
#print(dir(dict))
print(dict.keys())#displays only keys
print(dict.values())#displays only values
print(dict.items())#displays all items
print(dict["name1"])#access by key 






