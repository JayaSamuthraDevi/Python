
# #swapping two numbers
# a = 5
# b = 7
# a,b = b,a

# print(a,b)

#traverse by index
# fruits = ["apple", "orange", "grape", "kiwi"]
# for i in range(len(fruits)):
#     print(fruits[i])


#receiving list directly into respective variables
#brand model ram camera_pixel
# brand, model, ram, camera_pixel = ["redmi", "note", "12GB", "100MP"]

# students = {
#             1: "Student1",
#             2: "Student2"
#            }
# for key, value in students.items():
#     print(key, value)


#positive index, negative index, range index in list
fruits = ["apple", "orange", "grape", "kiwi"]
#           0         1        2        3
#           -4       -3       -2       -1
print(fruits[-2])
second_list = fruits[2:4]
print(second_list)

# #nested list (2*2 matrix, n*n matrix)
fruits = ["apple", [2,3,3], "grape", "kiwi"]
# vegetables = ["spinach", "carrot", "beetroot", "cabbage"]
# menu_list = [fruits, vegetables]
# print(menu_list)
# print(menu_list[0])
# print(menu_list[1][0])


#nested dictionary
students = {
             1: {"name": "student1", "age": 13, "class":"b"},
             2: {"name": "student2", "age": 13, "class":"a"}
            }
# print(students)
#dictionary containing lists

#list of dictionary
# students = [{"name": "student1", "age": 13, "class":"b"},{"name": "student2", "age": 13, "class":"a"}]
# print(students[1])


# # adding two lists
# number_list1 = [1,2,3]
# number_list2 = [3,4,5]
# number_list3 = number_list1 + number_list2
# print(number_list3)

# #combine two dictionaries
# student_detail1 = {"name": "student1", "age": 13, "class":"b"}
# student_detail1_additional = {"std": 5, "school":"someschool"}
# student_detail1.update(student_detail1_additional)
# print(student_detail1)



#list comprehension
#create a list of numbers from 1 to 20
numbers = [i for i in range(1,21)]
# print(numbers)
#create a list which contains square of numbers from 1 to 10
# square_numbers = [i*i for i in range(1, 11)]
# print(square_numbers)
#form odd number list from the above
odd_numbers = [i for i in numbers if i % 2 != 0]
print(odd_numbers)
# # print(odd_numbers)
# #form even number list from above list
# even_numbers = [i for i in numbers if i % 2 == 0]
# print(even_numbers)

