class User:
    user_list = []
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        User.add_new_user(self)
        pass
    
    def user_detail(self):
        return f'You are{self.name} and your a {self.gender}'
    

    @classmethod
    def add_new_user(cls, new_user):
        cls.user_list.append(new_user)
    

u1 =User("Brian", "Male")
u2 =User("Collins", "Male")
u3 =User("wendy", "Female")
# {
#     "name" : "Brian",
#     "gender" : "Male"
# }
print(u1.name) 
print(u1.gender)  
# print(u1.user details())     
print(User.user_list) 


for user in User.user_list:
    print(f'{user.name} {user.gender}')