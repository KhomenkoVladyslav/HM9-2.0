USERS = {}


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "User not found"
        except ValueError:
            return "Give me your name and phone please"
        except IndexError:
            return "Enter user name"

    return inner


def hello_user():
    return "How can I help you?"


def unknown_command():
    return "unknown_command"


def exit_command():
    return "Goodbye!"


@error_handler
def add_user(name, phone):
    USERS[name] = phone
    return f"User {name} added!"


@error_handler
def change_phone(name, phone):
    if name in USERS:
        old_phone = USERS[name]
        USERS[name] = phone
        return f"{name} має новий телефон: {phone} Старий номер: {old_phone}"
    else:
        return "User not found"


def show_all():
    if USERS:
        result = ""
        for name, phone in USERS.items():
            result += f"Name: {name} phone: {phone}\n"
        return result
    else:
        return "No users found"


@error_handler
def show_phone(name):
    if name in USERS:
        phone = USERS[name]
        return f"Phone number for {name}: {phone}"
    else:
        return "User not found"


HANDLERS = {
    "hello": hello_user,
    "add": add_user,
    "change": change_phone,
    "show all": show_all,
    "exit": exit_command,
    "good bye": exit_command,
    "close": exit_command,
}


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lower().strip()

    try:
        handler = HANDLERS[command]
    except KeyError:
        if args:
            command = command + " " + args[0]
            args = args[1:]
        handler = HANDLERS.get(command, unknown_command)
    return handler, args


def main():
    while True:
        user_input = input("Please enter command and args: ")
        handler, args = parse_input(user_input)
        result = handler(*args)
        print(result)
        if handler == exit_command:
            break


if __name__ == "__main__":
    main()
