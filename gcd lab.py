def gcd (a,b):
   
    while b:
        r=a%b
        a=b
        b=r
    return a
a=int(input("enter num1"))
b=int(input("enter num2"))
print(gcd(a,b))
