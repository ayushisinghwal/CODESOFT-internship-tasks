# Contact Book Application
contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False

    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True

    if not found:
        print("No matching contact found.\n")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            print("Leave blank to keep current value.")
            new_name = input(f"Enter new name [{contact['name']}]: ") or contact["name"]
            new_phone = input(f"Enter new phone [{contact['phone']}]: ") or contact["phone"]
            new_email = input(f"Enter new email [{contact['email']}]: ") or contact["email"]
            new_address = input(f"Enter new address [{contact['address']}]: ") or contact["address"]

            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully!\n")
            return

    print("No matching contact found.\n")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted successfully!\n")
            return

    print("No matching contact found.\n")

def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
