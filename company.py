class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = amount

    def work(self):
        return f'{self.name} is working'

    def annual_bonus(self):
        return self.salary * 0.05


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.team = []

    def add_team_member(self, team_member):
        if not isinstance(team_member, TechnicalMentor):
            raise TypeError("Team member must be an instance of Technicnal Mentor Object")
         
        self.team.append(team_member)

    def work(self):
        base = super().work()
        return f'{base} and managing {self.department}'


class TechnicalMentor(Employee):
    def __init__(self, name, salary, track):
        super().__init__(name, salary)
        self.track = track

    def work(self):
        return f'{self.name} is teaching {self.track}'


emp1 = Employee("Brian", 40000)
print(emp1.work())

mng = Manager("Rose", 50000, "Sinatre Pod")

tm1 = TechnicalMentor("Titus", 50000, "Software development")
tm2 = TechnicalMentor("Albert", 60000, "Data science")

mng.add_team_member("Jackyline")

# mng.add_team_member(tm1)
# mng.add_team_member(tm2)


print(mng.department)
print(mng.salary)
# print(mng.work())
print(tm1.work())
print(mng.name)
print(mng.team)

for tm in mng.team:
    print(tm.name)