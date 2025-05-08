class Student():
    def __init__(self, name, no):
        self.name = name #instance variable
        self.no = no #instance variable
        print('A student is created.')

s1 = Student('Hasan', 24)
s2 = Student('Arafat', 23)

print(s1)
print(s2) 