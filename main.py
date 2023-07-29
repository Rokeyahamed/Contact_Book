
contacts = {}
def add_contact():
    name = input("Enter name: ").capitalize()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print("Contact added successfully.\n")

def view_contacts():
    if contacts:
        print("CONTACT LIST:")
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details['phone'])
            print("Email:", details['email'])
            print()
    else:
        print("No contacts found.\n")

def search_contacts():
    search_query = input("Enter name or number to search: ").lower()
    matching_contacts = []

    for name, details in contacts.items():
        if search_query in name.lower() or search_query in details['phone']:
            matching_contacts.append((name, details['phone'], details['email']))

    if matching_contacts:
        print("MATCHING CONTACTS:")
        for contact in matching_contacts:
            name, phone, email = contact
            print("Name:", name)
            print("Phone:", phone)
            print("Email:", email)
            print()
    else:
        print("No matching contacts found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").capitalize()
    if name in contacts:
        print("CONTACT DETAILS:")
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
        print()
        confirm = input("Are you sure you want to delete this contact? (y/n): ")
        if confirm.lower() == 'y':
            del contacts[name]
            print("Contact deleted successfully.\n")
        else:
            print("Contact deletion canceled.\n")
    else:
        print("Contact not found.\n")

def edit_contact():
    name = input("Enter the name of the contact to edit: ").capitalize()
    if name in contacts:
        print("CONTACT DETAILS:")
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
        print()
        new_name = input("Enter new name : ").capitalize()
        new_phone = input("Enter new phone number : ")
        new_email = input("Enter new email : ")

        if new_name and new_name != name:
            contacts[new_name] = contacts.pop(name)
        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email

        print("Contact edited successfully.\n")
    else:
        print("Contact not found.\n")

while True:

    print("CONTACT BOOK")
    print("1. Add a Contact")
    print("2. View Contact List")
    print("3. Search Contacts")
    print("4. Delete a Contact")
    print("5. Edit a Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        edit_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.\n")
