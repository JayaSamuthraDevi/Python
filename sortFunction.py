list1=[2,10,3,1,6,4,7,9,0]

new_list=[]

while list1:
    min=list1[0]
    for x in list1:
        if min>x:
            min=x
    new_list.append(min)
    list1.remove(min)

print(new_list)