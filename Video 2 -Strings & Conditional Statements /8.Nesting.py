age=int(input("Enter age:"))
if(age>=18):
    if(age>=80):                                            #Nesting
        print("Can't drive")
    else:    
        print("Can drive")
elif(age<18):
    if(age==17):                                            #Nesting
        print("Wait",18-age ,"more year to drive.")
    else:
        print("Wait",18-age ,"more years to drive.")
        
        