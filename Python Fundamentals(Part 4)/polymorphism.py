            #1 Fuction overriding

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")  
        
        
t1 = Teacher()
t1.get_designation()
      
              #2 Duck Typing

class Teachers():
    def get_designations(self):
        print("designations = Teachers") 

class Accountants():
    def get_designations(self):
        print("designations = Accountants") 

t2 = Teachers()
t2.get_designations()

acc1 = Accountants()
acc1.get_designations()

