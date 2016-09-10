class Person(object):
    def __init__(self, name, age, username, email, password, wallet=0, salary=100, job=None, person_type=None):
        if person_type == 'Employee':
            self.salary = salary
            self.job = job
        self.name = name
        self.age = age
        self.username = username
        self.email = email
        self.password = password
        self.wallet = wallet
        self.logged_in = None
        self.saving_account = None
        self.checkings_account = None


class Employee(Person):
    pass


class Customer(Person):
    pass


