class Student:
    college="Hit Haldia"             #Common Attribute
    def __init__(self,name):
        self.name=name               #Another Attribute
s1=Student("Anindya Kumar")          
s2=Student("Anindya Roy")
print(s1.name,s1.college)
print(s2.name,s2.college)