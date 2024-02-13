import csv
from os import path


class Controller():
    DB_PATH = 'data/data.csv'

    def __init__(self) -> None:
        self.create_db()

    def create_db(self):
        '''
        create db
        '''
        if not path.exists(self.DB_PATH):
            new_file = open(self.DB_PATH, 'w+')
            new_file.close()

    def read_db(self):
        """
        File reading function.
        :return:
        """
        try:
            with open(self.DB_PATH, "r", newline="") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            return []

    def save_db(self, row: list, mod: str):
        """
        File saving function.
        :param row:
        :param mod:
        :return:
        """
        fieldnames = ('sur_name', 'first_name', 'middle_name', 'organization', 'work_phone', 'personal_phone', 'address', 'email')

        with open(self.DB_PATH, mod, newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if mod == 'w': writer.writeheader()
            writer.writerows(row)
        
        return True

    def add_entry(self, row: list):
        return self.save_db(row, 'a')
    def edit_entry(self, row: list):
        return self.save_db(row, 'w')

