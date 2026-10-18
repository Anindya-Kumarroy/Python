with open("Practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Python","Cpp")
print(new_data)