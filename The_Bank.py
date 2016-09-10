from Person import Employee, Customer
from validations import Validations

class Bank(object):
    def __init__(self):
        self.list_of_customers = []
        self.list_of_employees = []

    def _add_person_to_list(self, alist, person):
        alist.append(person)
        return alist

    def _check_if_is_employee_of_bank(self, employee):
        if employee in self.list_of_employees:
            return employee
        else:
            print "Can't do that action because {} is not an employee of the bank".format(employee.name)

    def pay_employee(self, employee):
        self._check_if_is_employee_of_bank()
        employee.salary += employee.checkings_account

    def fire_employee(self, employee):
        self._check_if_is_employee_of_bank(employee)
        self.list_of_employees.remove(employee)

    def give_raise(self, employee, amoumt_to_raise):
        self._check_if_is_employee_of_bank(employee)
        employee.salary += amoumt_to_raise

    def find_employee(self, employee):
        self._check_if_is_employee_of_bank(employee)
        return employee



class Account(object):
    def __init__(self, customer, account_number):
        self.withdraw_saving_account_fee = 2
        customer.account_number = account_number
        customer.saving_account_balance = 0
        customer.checkings_account_balance = 0
        customer.checkings_account = 'Checkings_account'
        customer.saving_account = 'Savings_account'

    def login(self, customer, ):
        username = raw_input("Enter you'r Username: ")
        password = raw_input("Enter you'r Password: ")
        if customer.username == username and customer.password == password:
            customer.logged_in = True
        elif customer.username is not username and customer.password is not password:
            customer.logged_in = False
        return customer.logged_in

    def withdraw(self, customer, amount_to_withdraw, type_of_account=None):
        """

        :param customer: Object
        :param amount_to_withdraw: Int
        :param type_of_account: 'Savings_account', 'checkings_account'
        :return: Object
        """
        if customer.logged_in:
            if type_of_account == customer.saving_account:
                if customer.saving_account_balance > self.withdraw_saving_account_fee and amount_to_withdraw <= customer.saving_account_balance:
                    customer.saving_account_balance -= (self.withdraw_saving_account_fee + amount_to_withdraw)
                    customer.wallet += amount_to_withdraw
                    return customer
                else:
                    print 'You were unable to pay the withdraw fee'
            elif type_of_account == customer.checkings_account:
                if amount_to_withdraw < customer.checkings_account_balance:
                    customer.checkings_account_balance -= amount_to_withdraw
                    customer.wallet += amount_to_withdraw
                    return customer

    def deposit(self, customer, amount_to_deposit, type_of_account=None):
        """

        :return: Object
        :param customer: Object
        :param amount_to_deposit: Int
        :param type_of_account: 'Savings_account', 'checkings_account'
        """
        if customer.logged_in:
            if type_of_account == customer.checkings_account:
                customer.checkings_account_balance += amount_to_deposit
            elif type_of_account == customer.saving_account:
                customer.saving_account_balance += amount_to_deposit
            else:
                print 'You did not say what type of account to deposit to'
        return customer

    def show_balance(self, customer, type_of_account):
        """

        :param customer: Object
        :param type_of_account: 'Savings_account', 'checkings_account'
        """
        if customer.logged_in:
            if type_of_account == customer.saving_account:
                print "You have {} $'s in your Saving account".format(customer.saving_account_balance)
            elif type_of_account == customer.checkings_account:
                print "You have {} $'s in your checking account".format(customer.checkings_account_balance)


