from The_Bank import Bank, Account
from Person import Employee, Customer
from uilities import *


if __name__ == '__main__':
	bank_of_israel = Bank()
	omri = Employee('omri',22,'omri.g@bank.com')
	nevo = Customer('nevo',21,'nevo.c@bank.com')
	while True:
		print_massage(Bank_managers_options)
		action = raw_input('What would your like to do: ')
		if action.lower() == 'p':
			bank_of_israel.pay_employee(omri)
			print omri.salary
			print omri.wallet
		else:
			break