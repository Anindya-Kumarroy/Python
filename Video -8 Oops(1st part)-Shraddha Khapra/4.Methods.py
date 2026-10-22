class Student:
    def __init__(self,name,marks):
        self.name=name                 #Attribute
        self.marks=marks
    def welcome(self):
        print("Hello ",self.name)
    def get_marks(self):               #Method
        return self.marks
s1=Student("Anindya Kumar!",98)
s1.welcome()
print("Your marks is:",s1.get_marks())