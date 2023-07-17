def bin_search(arr,target):
    low=0
    high=len(arr)
    while low<high:
        x=low+(high-low)//2
        val=arr[x]
        if target==val:
            return x
        elif target>val:
            if low==x:
                break
            low=x
        elif target<val:
            high=x

list1=(1,2,3,4,5,6)
print(bin_search(list1,3))