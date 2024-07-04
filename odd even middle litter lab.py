def odd_even(a):
    if len(a)%2==0:
        mid=len(a)//2
        ans=a[mid-1]+a[mid]
        return ans
    else:
        mid=len(a)//2
        ans=a[mid]
        return ans


a=input("enter a string")
print(odd_even(a))
