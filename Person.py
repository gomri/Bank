from validations import Validations

class Person(object):

    def __init__(self, name, age, email, wallet=0, salary=100, job=None, person_type=None):
        '''

        Validations() a class the validates password and username and creates team
        :param name:
        :param age:
        :param username:
        :param email:
        :param password:
        :param wallet:
        :param salary:
        :param job:
        :param person_type:
        '''
        validation = Validations()

        if person_type == 'Employee':
            self.salary = salary
            self.job = job
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
    pass


class Customer(Person):
    pass

omri = Employee('omri',22,'omri.g@test.com')
print omri.username
print omri.password

