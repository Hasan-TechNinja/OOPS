# class Teacher():
#     def __int__(self, name, id):
#         self.name = name
#         self.id = id
#         print('Running Init')

#     def details(self):
#         print(f"Name: {self.name}, ID: {self.id}")

# t1 = Teacher('Hasan', 23)

# print(t1)


class Teacher():
    def __init__(self, name, id):
        self.name = name #instance variable
        self.id = id #instance variable
        print('A student is created.')

    def details(self):
        print(f"Name: {self.name}, ID: {self.id}")

t1 = Teacher('Hasan', 24)
t2 = Teacher('Arafat', 23)

t1.details()
t2.details()