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
# print(s1.first_name)  
# print(Student.student_count)
# print(s1.greet())
# print(s2.greet())
# print(Student.student_count)
# print(Student.student_list)


# for student in Student.student_list:
#     print(student.first_name)



class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        

    def start(self):
        return("Vehicle starting........")    

class Car(Vehicle):
    def __init__(self, brand, model, wheels):
        super(). __init__(brand)
        self.model = model
        self._wheels = wheels

        @property
        def wheels(self):
            return self.wheels
        
        @wheels.setter
        def wheels(self, number_of_wheels):
            if number_of_wheels < 0:
                raise ValueError("Number of wheels cannot be less than zero")
            self._wheels = number_of_wheels
        
    def start(self):
        print(super().start())
        return(f'{self.brand} {self.model} with {self.wheels} wheels is ready to start ......')           


c1 = Car("Toyota", "Crown", -1)
# print(c1.brand)  
# print(c1.model)   
print(c1._wheels)
# print(c1.start())  


class Pet:

  def __init__ (self, name):
    self.name = name

buddy = Pet("Buddy")
