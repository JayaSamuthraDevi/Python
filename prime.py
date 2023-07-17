for num in range(100,201):
    if all(num%i!=0 for i in range(2,int(num/2)+1)):
        print(num,end=' ')