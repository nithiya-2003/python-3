a=input("enter the gender")
a=a.lower()
b=input("enter the martial status")
b=b.lower()
c=int(input("enter the annual income"))
print(a , b , c)

if(a == "female" and b =="married" and c<= 450000):
    print("women can get MAGALIR URIMAI THOGAI RS.5000 per month ")
else:
    print("sorry ,ROMBA THAAN AASAI!! ")
