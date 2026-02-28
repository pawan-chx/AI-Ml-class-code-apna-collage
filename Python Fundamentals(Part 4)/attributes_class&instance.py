                          #Attributes
   #class & instance    class => belong to class and instance => belog to object

class Student: 
    college_name = "abc college"   #class attribute

    def __init__(self, name, cgpa):
        self.name = name  #instance attribute
        self.cgpa = cgpa  #instance attribute
        

stu1 = Student("Pawan", 9.0)

print(stu1.name)
print(stu1.college_name)