from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def __str__(self):
        return self.value

    def validate(self, value: str):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError('Phone should be 10 digits')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number: str):
        result = False
        for phone in self.phones:
            if phone.value == phone_number:
                result = True
                return phone

        if result == False:
            return None

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            raise ValueError

    def remove_phone(self, rem_phone):
        for phone in self.phones:
            if phone.value == rem_phone:
                self.phones.remove(phone)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

# ----------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
