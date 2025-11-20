class GroceryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shopper:
    def __init__(self, name):
        self.name = name
        self.grocery_items = []


#Create a shopper and some grocery items
shopper = Shopper("Alice")
item1 = GroceryItem("apple", 1)
item2 = GroceryItem("orange", 2)

# Add the grocery items to the shopper's list
shopper.grocery_items.append(item1)
shopper.grocery_items.append(item2)

# Print the shopper's grocery list
for item in shopper.grocery_items:
    print(item.name, item.price)

# => apple 1
# => orange 2  
# 
# 


class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

# Create teachers
mr_smith = Teacher("Mr. Smith")
ms_jones = Teacher("Ms. Jones")

# Create students
alice = Student("Alice", 10)
bob = Student("Bob", 12)
carol = Student("Carol", 11)

# Assign students to teachers
mr_smith.add_student(alice)
mr_smith.add_student(bob)
ms_jones.add_student(carol)

# Check students for each teacher
print([s.name for s in mr_smith.students()])  # ['Alice', 'Bob']
print([s.name for s in ms_jones.students()])  # ['Carol']

# Access teacher from a student
print(alice.teacher.name)  # 'Mr. Smith'
