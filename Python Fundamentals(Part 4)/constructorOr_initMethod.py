                  #CONSTRUCTOR
 #  __init__Method        wo jo kisi bhi object ko creat karne ka kaam karta hai

class Student:
    village = "Andi"
    school = "Upgraded high school andi"

    # def __init__(self):  #default constructor
    #     print("/....")

    def __init__(self, name, subject, cgpa):  #parameterized constructor    kyun ki isme multiple parameters hai
        self.name = name
        self.subject = subject
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
    
    #most important ham ek class me do constructor nahi bana sakte hai agar bana hai to niche wala run karega


stu1 = Student("Pawan chauhan", "Python", 9.0)
stu2 = Student("Vishnu chauhan", "English", 8.0)
stu3 = Student("Ranjan chauhan", "Physics", 8.5)

print(stu1.village, stu1.cgpa)
print(stu2.school, stu2.name)
print(stu3.village, stu3.subject)
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()} and school is {stu1.school}")
