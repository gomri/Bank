class Person(object):
    def __init__(self, name, age, username, email, password, salary=100, job=None, person_type=None):
        if person_type == 'Employee':
            self.salary = salary
            self.job = job
        self.name = name
        self.age = age
        self.username = username
        self.email = email
        self.password = password


class Employee(Person):
    pass


class Customer(Person):
    pass


omri = Employee('omri', 22, 'omri.g', 'omri.g@test.com', 123456, person_type='Employee')
mayah = Customer('omri', 22, 'omri.g', 'omri.g@test.com', 89879)
print omri.salary
print mayah.password
