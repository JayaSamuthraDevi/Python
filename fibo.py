# n1=0
# n2=1
# print(n1,n2,end=" ")
# for i in range(3,10):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end=' ')



def Fibo(num):
    if num==0: return 0
    elif num==1: return 1
    else : return Fibo(num-1)+Fibo(num-2)

for i in range(16):
    print(Fibo(i),end=' ')