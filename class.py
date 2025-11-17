class Student:
    # class attributes => belongs to the whole class
    student_list = []
    student_count = 0
    def __init__(self, first_name, last_name):
        # instance attribute => unique to all objects
        self.first_name = first_name
        self.last_name = last_name
        self.track_student_count()
        Student.add_new_student(self)

    def greet(self):
        return(f'hello {self.first_name} {self.last_name}')    

    @classmethod
    def track_student_count(cls):
        cls.student_count += 1

    @classmethod
    def add_new_student(cls, new_student):   
        cls.student_list.append(new_student) 


s1 = Student('brian', 'kimno') 
s2 = Student('eunice', 'onkundi')  
s3 = Student('yvone', 'kadenyi') 
s4 = Student('thomas', 'mbula') 
print(s1.first_name)  
# print(Student.student_count)
print(s1.greet())
print(s2.greet())
print(Student.student_count)
print(Student.student_list)


for student in Student.student_list:
    print(student.first_name)


    