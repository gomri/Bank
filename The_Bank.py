from Person import Employee, Customer

class Bank(object):
    def __init__(self):
        self.customer = []
        self.accounts = []
        self.list_of_employees = []

    def _add_person_to_list(self, alist, person):
        alist.append(person)
        return alist

    def pay_employee(self, employee):
        employee.salary += employee.wallet


class Account(object):
    def __init__(self,customer, account_number):
        self.withdraw_saving_account_fee = 2
        customer.account_number = account_number
        customer.saving_account_balance = 0
        customer.checkings_account_balance = 0
        customer.checkings_account = 'Checkings_account'
        customer.saving_account = 'Savings_account'


    def login(self, customer,):
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
        if customer.loged_in and amount_to_withdraw <= customer.saving_account_balance:
            if type_of_account == customer.saving_account:
                if customer.checkings_account_balance > self.withdraw_saving_account_fee:
                    customer.checkings_account_balance - self.withdraw_saving_account_fee
                    customer.saving_account_balance -= amount_to_withdraw
                    customer.wallet += amount_to_withdraw
                    return customer
                else:
                    print 'You were unable to pay the withdraw fee'
            elif type_of_account == customer.checkings_account:
                if amount_to_withdraw <= customer.checkings_account_balance:
                    customer.checkings_acount_balance -= amount_to_withdraw
                    customer.wallet += amount_to_withdraw
                    return customer

    def deposit(self, customer, amount_to_deposit, type_of_account=None):
        """

        :return: Object
        :param customer: Object
        :param amount_to_deposit: Int
        :param type_of_account: 'Savings_account', 'checkings_account'
        """
        if customer.loged_in:
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
        if customer.loged_in:
            if type_of_account == customer.saving_account:
                print "You have {} $'s in your Saving account".format(customer.saving_account_balance)
            elif type_of_account == customer.checkings_account:
                print "You have {} $'s in your checking account".format(customer.Checkings_account_balance)




bank_israel = Bank()
omri = Employee('omri',19,'omri.g','omri.g@goroomer.com','123456',person_type='Employee')
# print omri.wallet
# print omri.salary
# print type(omri.password)
# print type(omri.username)
#
bank_of_israel_accouts = Account(omri,22)
# bank_of_israel_accouts.login(omri)
# print omri.logged_in
#
#
#
# bank_israel._add_person_to_list(bank_israel.list_of_employees,omri)
# print bank_israel.list_of_employees

