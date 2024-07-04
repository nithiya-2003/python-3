s1=int(input("enter the sub1:"))
s2=int(input("enter the sub2:"))
s3=int(input("enter the sub3:"))
s4=int(input("enter the sub4:"))
s5=int(input("enter the sub5:"))
    
def mark_range_validation(m):
    
    if m<=100 and m>90:
        return("O")
    elif m<=90 and m>80:
        return("A+")

    elif m<=80 and m>70:
        return("A")
    elif m<=70 and m>60:
        return("B")
    elif m<=60 and m>=50:
        return("C")
    elif m<50:
        return("fail")
    else:
        return("NR")
print("=============================================")
print("sub name","\t","marks","\t","grades")
print("=============================================")
print("s1","\t\t",s1,"\t",mark_range_validation(s1))
print("s2","\t\t",s2,"\t",mark_range_validation(s2))
print("s3","\t\t",s3,"\t",mark_range_validation(s3))

print("s4","\t\t",s4,"\t",mark_range_validation(s4))

print("s5","\t\t",s5,"\t",mark_range_validation(s5))
total=s1+s2+s3+s4+s5

avg=total/5
print("==============================================")
if (s1>50)and(s2>50)and(s3>50)and(s4>50)and(s5>50):
    print("result","\t\t",total,"\t",mark_range_validation(avg))
else:
    print("result","\t\t",total,"\t","fail")
print("==============================================")
