from The_Bank import Bank,Account
from Person import Employee,Customer

class Setup(object):

    def __init__(self):
        bank_of_israel = Bank()
        omri           = Employee('omri',22,'omri.g','omri.g@test.com',123456,person_type='Employee')
        mayah          = Employee('mayah', 25, 'mayah.g', 'mayah@test.com', 789456, person_type='Employee')




# if __name__ == '__main__':
#     while True: