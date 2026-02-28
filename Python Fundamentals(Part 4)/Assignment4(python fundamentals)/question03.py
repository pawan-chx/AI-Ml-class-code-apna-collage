class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)



    def get_marks(self):
        return self.__marks
        
    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Marks cannot be negative")   


    def get_roll_no(self):
        return self.__roll_no
        
    def set_roll_no(self, new_roll_no):
        if 1 <= new_roll_no <= 100:
            self.__roll_no = new_roll_no
        else:
            print("Invalid roll number")



    def get_name(self):
         return self.__name
 
         
    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            print("Name cannot be empty")



s1 = Student("pawan chauhan", 2, 98)

s1.set_marks(99)
s1.set_name("pawan kumar")
s1.set_roll_no(1)

print(s1.get_marks())
print(s1.get_roll_no())
print(s1.get_name())