student={
    "Name":"Anindya Kumar",
    "subjects" :{                     #Nested Dictionary. Remember the ':' in place of '=' 
        "DSA":99,
        "COA":88,
        "Digital E":96,
        "Math":85,
        "Economics":94
        
        
    }
}
print(student.keys())                 # student.keys() -> printing all the keys.
print(student.values())               # student.values() -> printing all the values.
print(student.items())                # student.items() -> all pairs returned.
pair=list(student.items())            # another process -> it must be in list form.
print(pair[0])

print(student.get("Name"))            # if we write somwthing as key which doesn't exist, still there eill be no error. It will simply print none. And codes after it will be printed.
                                      
print(student.get("Name2"))           # output -> none    

student.update({"City":"Delhi"})      # New value will be added.
print(student)                                 