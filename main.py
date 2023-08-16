ADDRESSBOOK = {}


def add_handler(data: list):
    name = data[0].upper()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with {phone} was saved"


def change_handler(data: list):
    name = data[0].upper()
    new_phone = data[1]
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name] = new_phone
        return f"Phone number for {name} was changed to {new_phone}"
    else:
        return f"No contact with name {name}"


def show_all_handler(*args):
    if ADDRESSBOOK:
        return "".join([f"{name}: {phone}" for name, phone in ADDRESSBOOK.items()])
    else:
        return "ADDRESSBOOK is empty"


def exit_handler(*args):
    return "Goodbye"


def hello_handler(*args):
    return "Hello"


def command_parser(raw_str: str):
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements[1:]


COMMANDS = {
    add_handler: ["add", "+"],
    change_handler: ["change"],
    show_all_handler: ["show all"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
}


def main():
    while True:
        user_input = input("<<<<<")
        if not user_input:
            continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        if user_input == "Hello":
            print("How can i help you?")


if __name__ == "__main__":
    main()
