from database import Database

class ClientModel:
    def __init__(self):
        self.db = Database()

    def generate_client_code(self, name):
        prefix = ''.join(word[0].upper() for word in name.split()[:3])  # Get first letters of up to 3 words
        if len(prefix) < 3:
            prefix = name[:3].upper()  # If name is short, take first 3 letters
        
        # Ensure uniqueness: Find the highest existing numeric suffix
        query = "SELECT client_code FROM clients WHERE client_code LIKE %s ORDER BY client_code DESC LIMIT 1"
        result = self.db.execute(query, (prefix + "%",), fetch=True)
        
        if result:
            last_code = result[0]['client_code']
            last_number = int(last_code[len(prefix):])  # Extract numeric part
            new_number = last_number + 1
        else:
            new_number = 1
        
        return f"{prefix}{new_number:03d}"  # Format as PREFIX001, PREFIX002, etc.

    def create_client(self, name):
        client_code = self.generate_client_code(name)  # Auto-generate client code
        query = "INSERT INTO clients (name, client_code) VALUES (%s, %s)"
        self.db.execute(query, (name, client_code))
        print(f"Client created successfully! Client Code: {client_code}")

    def get_all_clients(self):
        query = """
            SELECT clients.id, clients.name, clients.client_code, 
            COALESCE(COUNT(client_contacts.contact_id), 0) AS linked_contacts
            FROM clients
            LEFT JOIN client_contacts ON clients.id = client_contacts.client_id  -- Ensure correct linking
            GROUP BY clients.id, clients.name, clients.client_code
            ORDER BY clients.name ASC
        """
        return self.db.execute(query, fetch=True)


    def close(self):
        self.db.close()

