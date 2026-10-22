class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"your average score is:",sum/3)
s1=Student("Anindya Roy!",[98,96,94])
s1.get_average()