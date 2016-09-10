from validations import Validations


class Person(object):
    def __init__(self, name, age, email, wallet=0, person_type=None):
        """

        Validations() a class the validates password and username and sets them
        :param name:
        :param age:
        :param username:
        :param email:
        :param password:
        :param wallet:
        :param salary:
        :param job:
        :param person_type:
        """
        validation = Validations()
        self.person_type = person_type
        self.name = name
        self.age = age
        self.email = email
        self.username = validation.username_check()
        self.password = validation.password_check()
        self.wallet = wallet
        self.logged_in = None
        self.saving_account = None
        self.checkings_account = None


class Employee(Person):
    def __init__(self, name, age, email, salary=100, job=None,):
        super(Employee, self).__init__(name, age, email, person_type='Employee')
        self.salary = salary
        self.job = job


class Customer(Person):
    def __init__(self, name, age, email):
        super(Customer, self).__init__(name, age, email, person_type='Customer')

omri = Employee('omri', 22, 'omri.g@test.com')
mayah = Customer('omri', 22, 'omri.g@test.com')
print omri.salary
print omri.wallet
print omri.person_type
print mayah.person_type
