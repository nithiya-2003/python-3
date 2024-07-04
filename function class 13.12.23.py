#def fun_name():
    #print("hello")
    #print("dm")
#print("hi")
#fun_name()
#fun_name()
#def fun_ascii():
    #a=input("enter a value:")
    #print(a,"=",ord(a),)
    
#fun_ascii()
#def fun_hi(a):
 #   print(ord(a))
#a=input("enter a value")
#fun_hi(a)
def fun_sirascii(li):
    for i in li:
        print(i,"=",ord(i))
    
#li="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#fun_sirascii(li)
              
#a=int(input(" nmb"))
             
def fun_arith(choice):
    if choice=="+":
        c=a+b
        print(c)
    else :
        if choice=="-":
            c=a-b
            print(c)
        else:
            if choice=="*":
                 c=a*b
                 print(c)
            else:
                 if choice=="/":
                     c=a/b
                     print(c)
                 else :
                     if choice=="%":
                         c=a%b
                         print(c)
                     else:
                         print("sorry your choice is  not here")
                         
choice=input("""enter your choice":
             here your choice are...
             choice(+)
             choice(-)
             choice(*)
             choice(%)
             choice(/)""")
a=int(input("enter anumber"))
b=int(input("enter a another number"))
fun_arith(choice)      
