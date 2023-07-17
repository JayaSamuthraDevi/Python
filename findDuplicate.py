list1=[2,3,4,2,5,1,4,5,8,9,0,6,5,5,3]
#print duplicates
print(set([x for x in list1 if list1.count(x)>1]))


#removes duplicate
print(set(list1))