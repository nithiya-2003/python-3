   

def max_in_list(li):
    max=li[0]
    for j in range(0,len(li)):
       if li[j] >= max:
           max=li[j]
    return max



n=int(input("enter the value"))
li=[]

for i in range(n):
    li.append(int(input("enter the element")))
print(max_in_list(li)) 
