contacts = {}

def add_contact(name, number):
    contacts[name] = number

def view_contacts():
    for name, number in contacts.items():
        print(f"{name}: {number}")

add_contact('Alice', '123-456-7890')
add_contact('Bob', '987-654-3210')
view_contacts()
