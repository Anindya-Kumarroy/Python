class Student:
    def __init__(self, name,marks):  # self অবশ্যই দিতে হবে
        self.name = name
        self.marks=marks

s1 = Student("Anindya Roy",98)
print("Your name is", s1.name,"\nMarks:",s1.marks)

s2 = Student("Anindya Kumar",96)
print("Your name is", s2.name,"\nMarks:",s2.marks)