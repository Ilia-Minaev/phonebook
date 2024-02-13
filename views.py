from controller import Controller


class Views():
    def start_menu(self):
        """
        start menu.
        """
        error = 'Произошла ошибка. Заново введите нужный пункт меню:'
        print('''
    Меню телефонной книги:
    1. Показать записи
    2. Добавить новую запись
    3. Изменить запись
    4. Поиск записей
    5. Выход
        ''')

        choice = input('Введите пункт меню: ')
        try:
            choice = int(choice)
        except:
            print(error)

        if choice == 1:
            self.show_phonebook()
            self.nav_menu()
        elif choice == 2:
            self.add_or_edit_entry()
            self.nav_menu()
        elif choice == 3:
            self.add_or_edit_entry(edit=True)
            self.nav_menu()
        elif choice == 4:
            self.search_entries()
            self.nav_menu()
        elif choice == 5:
            print('До свидания!')
            exit()
        else:
            print(error)

    def show_phonebook(self):
        """
        showing all entries
        """
        controller = Controller()
        phonebook = controller.read_db()
        
        i = 1
        for item in phonebook:
            print(f'''==========================================
    ЗАПИСЬ №{i}
    Фамилия: {item['sur_name']}
    Имя: {item['first_name']}
    Отчество: {item['middle_name']}
    Организация: {item['organization']}
    Рабочий номер: {item['work_phone']}
    Личный номер: {item['personal_phone']}
    Адресс: {item['address']}
    email: {item['email']}
==========================================''')
            i += 1

    def add_or_edit_entry(self, edit: bool=False):
        """
        adding and editing entries
        :param edit:
        """
        check: bool = False
        if edit:
            try:
                inx = int(input('Введите номер изменяемой записи: ')) - 1
            except:
                print('Произошла ошибка! Попробуйде заново!')
                self.nav_menu()
        entry = {
            'sur_name': str(input('Введите фамилию: ')),
            'first_name': str(input('Введите Имя: ')),
            'middle_name': str(input('Введите Отчество: ')),
            'organization': str(input('Введите название огранизации: ')),
            'work_phone': str(input('Введите рабочий номер телефона: ')),
            'personal_phone': str(input('Введите личный номер телефона: ')),
            'address': str(input('Введите адресс: ')),
            'email': str(input('Введите email: ')),
        }
        controller = Controller()
        if edit:
            phonebook = controller.read_db()
            phonebook[inx] = entry
            check = controller.edit_entry(phonebook)

        else:
            check = controller.add_entry([entry])

        if check and edit:
            print('Запись изменена!')
        elif check and not edit:
            print('Запись добавлена!')
        else:
            print('Прозошла ошибка')

    def search_entries(self):
        """
        search entries
        """
        search_input = str(input('Введите поисковый запрос: ')).lower()
        controller = Controller()
        phonebook = controller.read_db()
        search_results = []

        for entry in phonebook:
            for key, val in entry.items():
                if str(val).lower() == search_input:
                    search_results.append(entry)
                    break

        for item in search_results:
            print(f'''==========================================
    Были найдены следующие записи:
    Фамилия: {item['sur_name']}
    Имя: {item['first_name']}
    Отчество: {item['middle_name']}
    Организация: {item['organization']}
    Рабочий номер: {item['work_phone']}
    Личный номер: {item['personal_phone']}
    Адресс: {item['address']}
    email: {item['email']}
==========================================''')

    def nav_menu(self):
        """
        return to the start menu
        """
        user_input = input('Вернуться в меню или завершить работу? Y/N ')
        try:
            user_input = str(user_input).lower()
        except:
            print('Произошла ошибка. Попробуйтей заново!')
            self.nav_menu()

        if user_input == 'y':
            self.start_menu()
        if user_input == 'n':
            print('До свидания!')
            exit()