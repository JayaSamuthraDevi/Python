
num=[i for i in range(1,21)]
print(num)

#list of squared values
squareNum=[i*i for i in range(1,21)]
print("Squared",num)


#only odd num 
oddNum=[i for i in num if i%2 != 0]
print("oddNum",oddNum)

#only even num 
evenNum=[i for i in num if i%2 == 0]
print("evenNum",evenNum)