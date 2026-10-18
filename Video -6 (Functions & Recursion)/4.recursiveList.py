def print_name(list,idx):
    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    
    print_name(list,idx+1)
    
names=["Anindya","Aradhya","moumita","Sunanda"]
print_name(names,0)
