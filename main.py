# Contact Management System

contacts = []

def show_menu():
    print("\n---Contact Management System---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n---Contact List---")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def search_contact():
    search_name = input("Enter contact name to search: ")
    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]
    if not found_contacts:
        print("No contacts found with that name.")
        return
    print("\n---Search Results---")
    for index, contact in enumerate(found_contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def delete_contact():
    view_contacts()
    if not contacts:
        return
    try:
        contact_index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            deleted_contact = contacts.pop(contact_index)
            print(f"Contact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")   


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()