def print_massage(massage):
    if type(massage) == str:
        print(massage)
    elif type(massage) == list:
        for i in range(len(massage)):
            print(massage[i])


Bank_managers_options = [
    'P - Pay employee',
    'F - Fire employee',
    'H - Hire employee',
    'C - Check if employee is working for the bank'
]

somethingtwo = 'somethingtwo'
