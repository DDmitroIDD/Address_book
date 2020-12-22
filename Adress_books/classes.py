from csv import DictReader, DictWriter


class Record:

    def __init__(self, phone_number, address=None):
        self.phone_number = phone_number  # this should be unique
        self.address = address

    def __str__(self):
        raise NotImplementedError

    @classmethod
    def from_csv(cls, fp):
        raise NotImplementedError


class Person(Record):
    def __init__(self, first_name, last_name, email, phone_number, address=None):
        super().__init__(phone_number, address)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # this should be unique

    @classmethod
    def from_csv(cls, fp):
        with open(fp) as db:
            for pers in DictReader(db):
                inform = [pers[' first_name'], pers[' last_name'], pers[' email'], pers[' phone'], pers[' address']]
                yield cls(*inform)


class Organization(Record):
    def __init__(self, name, category, phone_number, address):
        super().__init__(phone_number, address)
        self.name = name  # this should be unique
        self.category = category

    @classmethod
    def from_csv(cls, fp):
        with open(fp) as db:
            for org in DictReader(db):
                inform = [org[' name'], org[' category'], org[' phone'], org[' address']]
                yield cls(*inform)


class AddressBook:
    def __init__(self, fp):
        self.fp = fp

    def validate_person(self, data):
        with open(self.fp) as ad:
            emails = [i[' email'] for i in DictReader(ad)]
            if data in emails:
                return False
            return data

    def validate_org(self, data):
        with open(self.fp) as ad:
            names = [i[' name'] for i in DictReader(ad)]
            if data in names:
                return False
            return data

    def add_record(self, type_, data):
        with open(self.fp, 'a') as add_rec:
            writer = DictWriter(add_rec, fieldnames=[*data.keys()], restval='', lineterminator='\n')
            writer.writerow(data)
        print('Your data has been successfully entered')

    def find_record(self, type_, search_term):
        result = []
        with open(self.fp) as finder:
            if type_ == 'org':
                for i in DictReader(finder):
                    if i['type'] == 'Organization':
                        for j in i.items():
                            if search_term == j[1]:
                                result.append(j)
                if not result:
                    print('no matches found')
                else:
                    print(result)

            elif type_ == 'person':
                for i in DictReader(finder):
                    if i['type'] == 'Person':
                        for j in i.items():
                            if search_term == j[1]:
                                result.append(j)
                if not result:
                    print('no matches found')
                else:
                    print(result)

            else:
                for i in DictReader(finder):
                    for j in i.items():
                        if search_term == j[1]:
                            result.append(j)
                if not result:
                    print('no matches found')
                else:
                    print(result)

    def get_records(self, type_):
        with open(self.fp) as show:
            if type_ == 'org':
                for i in DictReader(show):
                    if i['type'] == 'Organization':
                        print(i)
            elif type_ == 'person':
                for i in DictReader(show):
                    if i['type'] == 'Person':
                        print(i)
            else:
                for i in DictReader(show):
                    print(i)

    def import_from_csv(self, fp):
        with open(self.fp,) as address_old_read:
            address_old_read = [i for i in DictReader(address_old_read)]
            with open(fp) as address_new:
                for line in DictReader(address_new):
                    for person_org in address_old_read:
                        if (person_org[' name'] == line[' name']) \
                                or (person_org[' email'] == line[' email']):
                            break
                        else:
                            with open(self.fp, 'a') as address_old_write:
                                writer = DictWriter(address_old_write, fieldnames=[*line.keys()],
                                                    restval='', lineterminator='\n')
                                writer.writerow(line)
