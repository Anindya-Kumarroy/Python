count=0
with open("p.txt","r") as f:
    data=f.read()
    print(data)
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print("Number of even numbers:",count)
    
