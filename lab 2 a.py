def dis(x1,x2,y31,y2):
    
    d=(x2-x1)**2+(y2-y1)**2
    
    dis=(d**0.5)#didtance
    return dis


x1=float(input("enter the value x1"))
x2=float(input("enter the value x2"))
y1=float(input("enter the value y1"))
y2=float(input("enter the value y2"))
print("the distance between two point is",dis(x1,x2,y1,y2))



#print("=====================================================================")
li=[]
c=[]
n=int(input("no of value"))#circulating valuesfor i in range(0,n):
li.append(int(input("enter the value")))
print(li)
m=int (input (" how many circulations "))
for j in range(1,m+1):
    b=li[j:]
    c=b+(li[:j])
print( "circulated values are",c,end=" ")
   
    
