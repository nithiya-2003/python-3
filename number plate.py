a={"TN":"Tamilnadu","DL":"Delhi"}
number=input("enter no")
i=number[:2]
if i in a:
    print(a[i])
else:
    print("state is not in dic")
