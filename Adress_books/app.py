import traceback
from datetime import datetime

from homework_oop.Adress_books import classes


def main():
    # CTRL + /
    address_book = classes.AddressBook('address_book.csv')
    print("Address book initialized. Source is: {}".format(address_book.fp))
    organizations = {}
    persons = {}

    while True:
        command = input("What you want to do? ADD, SHOW, FIND, EXIT ")
        """
        Validate input to check that input in these four: ADD, SHOW, FIND, EXIT
        1. Exit: close the program
        2. Add: add record
        3. Show: display records
        4. Find: find records
        """
        if command == 'ADD':
            """
            Ask user what type he want to add (org, person)
            based on this, ask required fields and check field uniqueness if required.
            After adding record show success message in console
            """

            type_ = input('What type you want to add: org or person? ')
            if type_ == 'org':
                phone_number = input('Please enter phone number of organization ')
                address = input('Please enter address of organization ')
                name = address_book.validate_org(input('Please enter name of organization '))
                while not name:
                    name = address_book.validate_org(input('This name is already in the book, '
                                                           'please enter another name '))
                category = input('Please enter category of organization ')
                data = {'type': 'Organization',
                        ' phone': phone_number,
                        ' address': address,
                        ' name': name,
                        ' category': category}
                organizations[name] = classes.Organization.from_csv(address_book)
                # organizations[name] = classes.Organization(name, category, phone_number, address)
                address_book.add_record(type_, data)

            if type_ == 'person':

                phone_number = input('Please enter phone number ')
                address = input('Please enter address ')
                first_name = input('Please enter first name ')
                last_name = input('Please enter last name ')
                email = address_book.validate_person(input('Please enter email '))
                while not email:
                    email = address_book.validate_person(input('This email is already in the book, '
                                                               'please enter another email '))
                data = {'type': 'Person',
                        ' phone': phone_number,
                        ' address': address,
                        ' first_name': first_name,
                        ' last_name': last_name,
                        ' email': email}
                persons[email] = classes.Person.from_csv(address_book)
                # persons[email] = classes.Person(first_name, last_name, email, phone_number, address)
                address_book.add_record(type_, data)

        if command == 'SHOW':
            """
            Ask type of records to show: org, person, all
            print records
            """
            type_ = input('What type of data to show: org, person, all? ')
            if 'person' != type_ != 'org':
                type_ = 'all'
            address_book.get_records(type_)
        if command == 'FIND':
            """
            Ask for type of records to find: org, person, all
            Ask for string to find any text, at least 5 symbols
            print results
            """
            type_ = input('What type of data to show: org, person, all? ')
            if 'person' != type_ != 'org':
                type_ = 'all'
            term = input('Write what you are looking for. A word of at least 5 characters ')
            while True:
                if len(term) < 5:
                    term = input('A word of at least 5 characters ')

                break
            address_book.find_record(type_, term)
        if command == 'EXIT':
            raise KeyboardInterrupt


if __name__ == '__main__':
    # Add try/except block to log every unhandled exception. (same as for lesson 4)
    try:
        main()
    except Exception as err:
        tb = traceback.format_exc()
        dt = str(datetime.now())
        log = f'{dt} | {err.__class__.__name__} \n {tb}'
        with open('logs.txt', 'a') as logs:
            logs.write(log)
    except KeyboardInterrupt as err:
        tb = traceback.format_exc()
        dt = str(datetime.now())
        log = f'{dt} | {err.__class__.__name__} \n {tb}'
        with open('logs.txt', 'a') as logs:
            logs.write(log)
