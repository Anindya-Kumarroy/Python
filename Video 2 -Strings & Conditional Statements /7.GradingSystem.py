marks=int(input("Enter marks:"))

if(marks>=80 and marks<=100):                       # && not used here. Instead and is used.
    print("Grade A")
elif(marks>=70 and marks<80):
    print("Grade B")
else:
    print("Failed")
    