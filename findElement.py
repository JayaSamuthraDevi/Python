def search(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            print("found")
            return i 
    print("Not found")


print(search((1,2,3,4,5,6),3) )      