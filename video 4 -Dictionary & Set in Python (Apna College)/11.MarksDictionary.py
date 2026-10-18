marks={}
x=int(input("Enter physics marks:"))
marks.update({"Physics:":x})

x=int(input("Enter chemistry marks:"))
marks.update({"Chemistry:":x})

x=int(input("Enter math marks:"))
marks.update({"Math:":x})

print(marks)