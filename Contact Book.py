# Contact Book

contact_book = {}

def add_contact(name, phone, email, address):
    if name in contact_book:
        print(f"Contact {name} already exists.")
    else:
        contact_book[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added.")

def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

def update_contact(name, phone=None, email=None, address=None):
    if name in contact_book:
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        if address:
            contact_book[name]['address'] = address
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if contact_book:
        print("Contact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("Contact book is empty.")

def search_contact(query):
    found = False
    for name, details in contact_book.items():
        if query.lower() in name.lower() or query in details['phone']:
            print(f"Found Contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print(f"No contact found for query: {query}")

# User Interface
def user_interface():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (leave blank if no change): ")
            email = input("Enter new email (leave blank if no change): ")
            address = input("Enter new address (leave blank if no change): ")
            update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            remove_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the user interface
user_interface()
