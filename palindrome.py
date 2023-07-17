# s=input()
# newS=""
# for i in range(len(s)-1,-1,-1):
#     newS=newS+s[i]

# if newS==s:
#     print("Palindrom",newS,"=",s)
# else:
#     print("not a palindrom",newS,"=",s)



def ispalin(s):
    rev =''.join(reversed(s))
    if (s==rev):
        return True
    return False

print(ispalin("abc"))