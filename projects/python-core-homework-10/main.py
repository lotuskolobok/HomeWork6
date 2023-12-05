from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)
    
    # додали getter для атрибутів value спадкоємців Field.
    @property
    def value(self):
        return self.__value

    # додали setter для атрибутів value спадкоємців Field.
    @value.setter
    def value(self, value):
        self.__value = value

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def __str__(self):
        return self.value
    
    def validate(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError('Phone should be 10 digits')

# додали клас Birthday, який наслідуємо від класу Field
class Birthday(Field):
    def __init__(self, value):
        super().__init__(self.validate(value))
        
    def validate(self, value):
        if value == None: 
            return None
        
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return value
        
        except ValueError:
            return None

# додали необов'язковий параметр birthday
class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # додали метод, який повертає значення параметра birthday
    def show_birthday(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday.value}"

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number: str):
        result = False
        for phone in self.phones:
            if phone.value == phone_number:
                result = True
                return phone
        
        if result == False:
            raise ValueError

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
    
    # додали ітератор
    def iterator(self, N):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}\n'
            counter += 1
            if counter >= N:
                yield result
                counter = 0
                result = ''

    

# ----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John", "2000-10-05")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane", "2001-02-20")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Створення та додавання нового запису для Sara
    sara_record = Record("Sara")
    sara_record.add_phone("5566997711")
    book.add_record(sara_record)

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

    # Виведення дати народження
    print(jane_record.show_birthday())
    print(john_record.show_birthday())
    print(sara_record.show_birthday())
    
    # Видалення запису Jane
    book.delete("Jane")
