n=int(input("num"))
for i in range (n):
    if i%3==0 and i%7==0:
        print(i)

a=input("enter a string")
b=a[::-1]
if b==a:
    print("palindrome")

else:
    print("not")

c={"60":"COIMBATORE","43":"NILGIRI "}
mumber=input("trajj")
mumber=mumber.upper()
num=mumber[3:5]
if mumber.startswith("TN"):
    if num in c:
        print(c[num])
    else:
        print("INVALID NUMBER")
        
