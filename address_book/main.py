import json

path_to_storage = 'storage.json'
exit_words = ['q', 'quit', 'exit']  # ключевые слова, для выхода из программы


class Person:
    """Класс для создания записи в адресную книгу"""

    def __init__(self, unique_id: str, first_name: str, last_name: str, address: str, telephone: str, email: str):
        self.id = unique_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.telephone = telephone
        self.email = email
        self.summary = dict()

        self.set_summary()

    def set_summary(self):
        self.summary = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'telephone': self.telephone,
            'email': self.email,
        }


def load_data_from_file() -> dict:
    with open(path_to_storage, 'r') as json_file:
        # Если в файле нет структуры json - создать для нее заготовку
        try:
            result = json.load(json_file)
        except ValueError:
            result = {'count_id': 0, 'persons': []}
        finally:
            return result


def save_data_to_file(dump: dict) -> None:
    with open(path_to_storage, 'w') as json_file:
        json.dump(dump, json_file, indent=4)


def get_next_id_from_file() -> str:
    current_data = load_data_from_file()
    next_id = current_data['count_id'] + 1
    current_data['count_id'] = next_id
    save_data_to_file(current_data)

    return str(next_id)


def add_person():
    print('Add person to address book (press "q" to exit)')

    first_name = input('First name: ')
    if first_name.lower() in exit_words:
        return
    last_name = input('Last name: ')
    if last_name.lower() in exit_words:
        return
    address = input('Address: ')
    if address.lower() in exit_words:
        return
    telephone = input('Telephone: ')
    if telephone.lower() in exit_words:
        return
    email = input('Email: ')
    if email.lower() in exit_words:
        return

    new_id = get_next_id_from_file()
    new_person = Person(new_id, first_name, last_name, address, telephone, email)
    current_data = load_data_from_file()
    current_data['persons'].append(new_person.summary)
    save_data_to_file(current_data)


def find_persons():
    current_data = load_data_from_file()
    search_phrase = input('Find person: ')

    matched_data = [p for p in current_data['persons'] if search_phrase in p.values()]

    max_i_len = 2   # 'ID'
    max_f_len = 10  # 'FIRST_NAME'
    max_l_len = 9   # 'LAST_NAME'
    max_a_len = 7   # 'ADDRESS'
    max_t_len = 9   # 'TELEPHONE'
    max_e_len = 5   # 'EMAIL'

    for p in matched_data:
        if len(p['id']) > max_i_len:
            max_i_len = len(p['id'])
        if len(p['first_name']) > max_f_len:
            max_f_len = len(p['first_name'])
        if len(p['last_name']) > max_l_len:
            max_l_len = len(p['last_name'])
        if len(p['address']) > max_a_len:
            max_a_len = len(p['address'])
        if len(p['telephone']) > max_t_len:
            max_t_len = len(p['telephone'])
        if len(p['email']) > max_e_len:
            max_e_len = len(p['email'])

    # шапка таблицы
    print(f'{"ID".rjust(max_i_len)}   {"LAST_NAME".rjust(max_l_len)}   {"FIRST_NAME".rjust(max_l_len)}   {"ADDRESS".rjust(max_a_len)}   {"TELEPHONE".rjust(max_t_len)}   {"EMAIL".rjust(max_e_len)}')

    for p in matched_data:
        i = p['id'].rjust(max_i_len)
        ln = p["last_name"].rjust(max_l_len)
        fn = p["first_name"].rjust(max_f_len)
        a = p["address"].rjust(max_a_len)
        t = p["telephone"].rjust(max_t_len)
        e = p["email"].rjust(max_e_len)

        print(f'{i}   {ln}   {fn}   {a}   {t}   {e}')


def delete_person():
    delete_id = input('Type ID person you want to remove: ')
    current_data = load_data_from_file()

    for p in current_data['persons']:
        if p['id'] == delete_id:
            print(f'Removing {p["first_name"]} {p["last_name"]} ')
            current_data['persons'].remove(p)
            save_data_to_file(current_data)


def modify_person():
    modify_id = input('Type ID person you want to modify: ')
    current_data = load_data_from_file()

    try:
        modifying_person = [p for p in current_data['persons'] if p['id'] == modify_id][0]
    except IndexError:
        print('No such person ID')
        return

    new_first_name = input(f'Change first name from "{modifying_person["first_name"]}" to: ')
    new_last_name = input(f'Change last name from "{modifying_person["last_name"]}" to: ')
    new_address = input(f'Change address from "{modifying_person["address"]}" to: ')
    new_telephone = input(f'Change telephone from "{modifying_person["telephone"]}" to: ')
    new_email = input(f'Change email from "{modifying_person["email"]}" to: ')

    for p in current_data['persons']:
        if p['id'] == modify_id:
            p['first_name'] = new_first_name
            p['last_name'] = new_last_name
            p['address'] = new_address
            p['telephone'] = new_telephone
            p['email'] = new_email

    save_data_to_file(current_data)


def print_full_address_book():
    current_data = load_data_from_file()

    max_i_len = 2   # 'ID'
    max_f_len = 10  # 'FIRST_NAME'
    max_l_len = 9   # 'LAST_NAME'
    max_a_len = 7   # 'ADDRESS'
    max_t_len = 9   # 'TELEPHONE'
    max_e_len = 5   # 'EMAIL'

    for p in current_data['persons']:
        if len(p['id']) > max_i_len:
            max_i_len = len(p['id'])
        if len(p['first_name']) > max_f_len:
            max_f_len = len(p['first_name'])
        if len(p['last_name']) > max_l_len:
            max_l_len = len(p['last_name'])
        if len(p['address']) > max_a_len:
            max_a_len = len(p['address'])
        if len(p['telephone']) > max_t_len:
            max_t_len = len(p['telephone'])
        if len(p['email']) > max_e_len:
            max_e_len = len(p['email'])

    # шапка таблицы
    print(f'{"ID".rjust(max_i_len)}   {"LAST_NAME".rjust(max_l_len)}   {"FIRST_NAME".rjust(max_l_len)}   {"ADDRESS".rjust(max_a_len)}   {"TELEPHONE".rjust(max_t_len)}   {"EMAIL".rjust(max_e_len)}')

    for p in current_data['persons']:
        i = p['id'].rjust(max_i_len)
        ln = p["last_name"].rjust(max_l_len)
        fn = p["first_name"].rjust(max_f_len)
        a = p["address"].rjust(max_a_len)
        t = p["telephone"].rjust(max_t_len)
        e = p["email"].rjust(max_e_len)

        print(f'{i}   {ln}   {fn}   {a}   {t}   {e}')


def main():

    while True:
        print('PLEASE, CHOOSE OPTION'.center(50, '-'))
        print('(1) Add, (2) Find, (3) Modify, (4) Delete, (0) Show all, (q) Exit')

        user_choice = input('YOU CHOICE: ')

        if user_choice == '1':
            print('ADD PERSON'.center(50, '-'))
            add_person()
        elif user_choice == '2':
            print('FIND PERSON'.center(50, '-'))
            find_persons()
        elif user_choice == '3':
            print('MODIFY PERSON'.center(50, '-'))
            modify_person()
        elif user_choice == '4':
            print('DELETE PERSON'.center(50, '-'))
            delete_person()
        elif user_choice == '0':
            print('SHOW ALL ADDRESS BOOK'.center(50, '-'))
            print_full_address_book()
        elif user_choice.lower() in exit_words:
            print('EXIT FROM ADDRESS BOOK'.center(50, '-'))
            return


if __name__ == '__main__':
    main()
