def linear_search(li,f):
    for j in li:
       if f==li[j]:
           return li.index(li[j])
    return False    




li=[]
n=int(input("enter  no of values"))
for i in range(n):
      li.append(int(input("enter the value for list:")))

f=int(input("enter the search element"))
print(linear_search(li,f))
