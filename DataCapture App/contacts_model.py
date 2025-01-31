from database import Database

class ContactModel:
    def __init__(self):
        self.db = Database()

    def create_contact(self, name, surname, email):
        query = "INSERT INTO contacts (name, surname, email) VALUES (%s, %s, %s)"
        self.db.execute(query, (name, surname, email))
        print("Contact created successfully!")

    def get_all_contacts(self):
        query = """
        SELECT c.id, c.surname, c.name, c.email, 
               (SELECT COUNT(*) FROM client_contacts WHERE contact_id = c.id) AS linked_clients
        FROM contacts c
        ORDER BY c.surname ASC, c.name ASC
        """
        return self.db.execute(query, fetch=True)

    def link_contact_to_client(self, contact_id, client_id):
        query = "INSERT INTO client_contacts (client_id, contact_id) VALUES (%s, %s)"
        self.db.execute(query, (client_id, contact_id))
        print(f"Contact {contact_id} linked to Client {client_id}.")

    def get_linked_clients(self, contact_id):
        query = """
        SELECT cl.name, cl.client_code
        FROM clients cl
        JOIN client_contacts cc ON cl.id = cc.client_id
        WHERE cc.contact_id = %s
        ORDER BY cl.name ASC
        """
        return self.db.execute(query, (contact_id,), fetch=True)

    def unlink_contact_from_client(self, contact_id, client_id):
        query = "DELETE FROM client_contacts WHERE client_id = %s AND contact_id = %s"
        self.db.execute(query, (client_id, contact_id))
        print(f"Contact {contact_id} unlinked from Client {client_id}.")

    def close(self):
        self.db.close()

