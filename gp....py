def geom_prog(a,d,n):
    
    for  i in range(n):
        u=d**i
        gp=a*u
        print(gp,end=" ")

a=int(input("enter the first element:"))
d=int(input("enter the common difference:"))
n=int(input("enter no of terms u want"))
geom_prog(a,d,n)
