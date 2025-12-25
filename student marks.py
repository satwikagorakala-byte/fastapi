class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
        if(self.marks>=35):
            return f"{self.name} with marks {self.marks} is Pass"
        else:
            return  f"{self.name} with marks {self.marks} is Fail"


s=Student("satwika", 33)
s.display()

class Student1:
    def display(self,name,marks):

        if(marks>=35):
            return f"{name} with marks {marks} is Pass"
        else:
            return  f"{name} with marks {marks} is Fail"



p=Student1()
p.display("satwika", 45)
