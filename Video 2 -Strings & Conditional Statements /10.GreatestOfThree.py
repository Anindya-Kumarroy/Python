a,b,c=map(int,input("Enter three numbers:").split())     #remember the process
print("Your inputted numbers:",a,b,c)

if(a>b and a>c):
    print("Biggest number is:",a)
elif(b>a and b>c):
    print("Biggest number is:",b)
else:
    print("Biggest number is:",c)
