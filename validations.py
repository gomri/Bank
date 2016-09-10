import re


class Validations(object):

    def username_check(self):
        """
        Verify the strength of 'username'
        Returns a dict indicating the wrong criteria
        A password is considered strong if:
            6 characters length or more
            1 digit or more
            1 uppercase letter or more
            1 lowercase letter or more
        """

        counter = 0
        while counter < 3:
            username = raw_input('Enter a Username: ')
            # calculating the length
            length_error = len(username) < 6

            # searching for digits
            digit_error = re.search(r"\d", username) is None

            # searching for uppercase
            uppercase_error = re.search(r"[A-Z]", username) is None

            # searching for lowercase
            lowercase_error = re.search(r"[a-z]", username) is None

            # searching for symbols
            symbol_error = re.search(r"\W", username) is None

            username_checks = {
                'length_error': length_error,
                'digit_error': digit_error,
                'uppercase_error': uppercase_error,
                'lowercase_error': lowercase_error
            }

            if username_checks.values().count(False) >= 3:
                return username
            elif username_checks.values().count(False) < 3:
                print "You'r password wasn't secure enough, you have {} more tries".format(2 - counter)
                counter += 1


    def password_check(self):
        """
        Verify the strength of 'password'
        Returns a dict indicating the wrong criteria
        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """
        counter = 0
        while counter < 3:
            password = raw_input('Enter a password: ')
            # calculating the length
            length_error = len(password) < 8

            # searching for digits
            digit_error = re.search(r"\d", password) is None

            # searching for uppercase
            uppercase_error = re.search(r"[A-Z]", password) is None

            # searching for lowercase
            lowercase_error = re.search(r"[a-z]", password) is None

            # searching for symbols
            symbol_error = re.search(r"\W", password) is None

            password_checks = {
                'length_error': length_error,
                'digit_error': digit_error,
                'uppercase_error': uppercase_error,
                'lowercase_error': lowercase_error,
                'symbol_error': symbol_error,
            }

            if password_checks.values().count(False) >= 3:
                return password
            elif password_checks.values().count(False) < 3:
                print "You'r password wasn't secure enough, you have {} more tries".format(2 - counter)
                counter += 1


