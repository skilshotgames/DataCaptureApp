from client_model import ClientModel

class ClientController:
    def __init__(self):
        self.model = ClientModel()
    
    def create_client(self):
        name = input("Enter client name: ").strip()

        if not name:
            print("Error: Client name is required.")
            return

        self.model.create_client(name)



    def view_clients(self):
        self.model.db.execute("COMMIT")  # Ensure database transactions are committed
        clients = self.model.get_all_clients()
        if clients:
            print("\nClients List:")
            print(f"{'ID':<5} {'Name':<25} {'Client Code':<10} {'Linked Contacts':^15}")
            print("=" * 60)
        else:
            print("No client(s) found.")

        for c in clients:
            print(f"{c['id']:<5} {c['name']:<25} {c['client_code']:<10} {c['linked_contacts']:^15}")

    def close(self):
        self.model.close()
