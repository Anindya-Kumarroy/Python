age=116
if(age>=18):
    print("Can vote")                            # 4 spaces needed. This is called indentation-proper spacing.
    print("Can drive")
else:                                            # : after conditional statement
    print("Can't vote or drive")
    
light=input("Enter the light color:")
if(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("Look")
else:
    print("Stop")