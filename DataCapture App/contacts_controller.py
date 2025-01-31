from contacts_model import ContactModel

class ContactController:
    def __init__(self):
        self.model = ContactModel()

    def create_contact(self):
        name = input("Enter contact's first name: ").strip()
        surname = input("Enter contact's surname: ").strip()
        email = input("Enter contact's email: ").strip()

        if name and surname and email:
            self.model.create_contact(name, surname, email)
        else:
            print("All fields are required!")

    def view_contacts(self):
        contacts = self.model.get_all_contacts()

        if not contacts:
            print("No contact(s) found.")
        else:
            print(f"{'ID':<5} {'Surname':<20} {'Name':<20} {'Email':<30} {'Linked Clients':^15}")
            print("=" * 95)
        for c in contacts:
            print(f"{c['id']:<5} {c['surname']:<20} {c['name']:<20} {c['email']:<30} {c['linked_clients']:^15}")




    def link_contact_to_client(self):
        contact_id = input("Enter Contact ID to link: ").strip()
        client_id = input("Enter Client ID to link: ").strip()

        if contact_id.isdigit() and client_id.isdigit():
            self.model.link_contact_to_client(int(contact_id), int(client_id))
        else:
            print("Invalid input. Please enter numeric IDs.")

    def view_linked_clients(self):
        contact_id = input("Enter Contact ID to view linked clients: ").strip()

        if contact_id.isdigit():
            linked_clients = self.model.get_linked_clients(int(contact_id))
            if not linked_clients:
                print("No linked clients found.")
            else:
                print(f"{'Client Name':<30} {'Client Code':<15}")
                print("="*45)
                for c in linked_clients:
                    print(f"{c[0]:<30} {c[1]:<15}")
        else:
            print("Invalid input. Please enter a numeric ID.")

    def unlink_contact_from_client(self):
        contact_id = input("Enter Contact ID to unlink: ").strip()
        client_id = input("Enter Client ID to unlink: ").strip()

        if contact_id.isdigit() and client_id.isdigit():
            self.model.unlink_contact_from_client(int(contact_id), int(client_id))
        else:
            print("Invalid input. Please enter numeric IDs.")

    def close(self):
        self.model.close()
