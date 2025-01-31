from client_controller import ClientController
from contacts_controller import ContactController

def main():
    client_controller = ClientController()
    contact_controller = ContactController()
    
    while True:
        print("\nMain Menu:")
        print("1. Manage Clients")
        print("2. Manage Contacts")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            manage_clients(client_controller)
        elif choice == "2":
            manage_contacts(contact_controller)
        elif choice == "3":
            client_controller.close()
            contact_controller.close()
            break
        else:
            print("Invalid choice! Please try again.")

def manage_clients(controller):
    while True:
        print("\nClient Management:")
        print("1. Create Client")
        print("2. View Clients")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            controller.create_client()
        elif choice == "2":
            controller.view_clients()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.")

def manage_contacts(controller):
    while True:
        print("\nContact Management:")
        print("1. Create Contact")
        print("2. View Contacts")
        print("3. Link Contact to Client")
        print("4. View Linked Clients")
        print("5. Unlink Contact")
        print("6. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            controller.create_contact()
        elif choice == "2":
            controller.view_contacts()
        elif choice == "3":
            controller.link_contact_to_client()
        elif choice == "4":
            controller.view_linked_clients()
        elif choice == "5":
            controller.unlink_contact_from_client()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

