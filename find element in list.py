li=[2,3,4,5,6,8,10,9]
def fun_find(li,n):
    for i in li:
        if(n==i):
            return(li.index(i))
    return-1

li=[2,3,4,5,6,8,10,9]
n=int(input("enter a number"))
print(fun_find(li,n))



