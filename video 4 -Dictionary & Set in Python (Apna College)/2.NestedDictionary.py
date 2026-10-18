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

print(student["Name"])
print(student["subjects"]["DSA"])      #For printing specific element of nested sictionary.
print(student["subjects"])             #For printing nested dictionary.
print(student)                         #Printing the whole dictionary