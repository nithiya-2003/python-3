a=input("enter a mail")
an=0
l=0
bat=0
b=0
sp=0
i=0
for i in a:
    if i.isalnum():
        an=an+1
        
    elif i.islower():
        l=l+1

            
    elif(i=="@"):
        bat=bat+1
        
    else:    
        sp=sp+1


                
if(an>=1)and(bat==1)and(l>=1)and (sp>=1):
    print("given mail id is g mail")
else:
    print("given mail id is not a g mail id")
                
