phone_book = {}
exit_cmd = ['good bye', 'close', 'exit', 'quit', 'end']

def input_error(Exception):
    try:
        pass

    except ValueError:
        print ('-=ERROR-=: Incorrect value')

    except KeyError:
        print ('-=ERROR-=: Enter user name')

    except IndexError:
        print ('-=ERROR-=: Incorrect count of args')

    except Warning:
        print ('-=ERROR-=: Incorrect command')

def add_phone(my_string: str):
    tmp = my_string.split()
    if len(tmp) == 2:
        name = tmp[0]
        phone = tmp[1]
        if phone.isdigit() == True:
            phone_book[name] = phone
        else:
            raise ValueError

        return f'For name "{name}" added phone "{phone}"'

    else:
        raise IndexError

def change_phone(my_string:str):
    tmp = my_string.split()
    if len(tmp) == 2:
        name = tmp[0]

        phone_old = phone_book[name]

        if phone_old == None:
            raise ValueError

        phone = tmp[1]
        if phone.isdigit() == True:
            phone_book[name] = phone
        else:
            raise KeyError

        return f'For name "{name}" phone "{phone_old}" changed to "{phone}"'

    else:
        raise IndexError

def phone_show(my_string: str):
    tmp = my_string.split()
    if len(tmp) == 1:
        name = tmp[0].strip()
        phone = phone_book[name]

        return f'For name "{name}" phone is {phone}'

    else:
        raise IndexError



@input_error
def call_bot():
    
    while True:
        is_break = False
        command = input('Enter your command: ').lower()

        if command == 'hello':
            result = 'How can I help you?'
        elif command in exit_cmd:
            result = '-'*10 + '\nBye-Bye!:)\n' + '-'*10
            is_break = True
        elif command.startswith('add'):
            result = add_phone(command.removeprefix('add'))
        elif command.startswith('change'):
            result = change_phone(command.removeprefix('change'))
        elif command.startswith('show all'):
            result = phone_book
        elif command.startswith('phone'):
            result = phone_show(command.removeprefix('phone'))
        else:
            raise Warning

        print (result)

        if is_break:
            break


if __name__ == '__main__':

    call_bot()