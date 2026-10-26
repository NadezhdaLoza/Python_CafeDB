from utils.database import execute_query

class ClientRepository:
    def find_all(self):
        query = """
            SELECT c.client_id, 
                   c.last_name,
                   c.first_name,
                   c.middle_name,
                   c.last_name || ' ' || c.first_name || ' ' || COALESCE(c.middle_name, '') as full_name,
                   c.phone,
                   c.card_id,
                   bc.card_number
            FROM clients c
            LEFT JOIN bonus_cards bc ON c.card_id = bc.card_id
            ORDER BY c.last_name ASC
        """
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = """
            SELECT c.client_id, c.last_name, c.first_name, c.middle_name, c.phone,
                   bc.card_id, bc.card_number, bc.balance
            FROM clients c
            LEFT JOIN bonus_cards bc ON c.card_id = bc.card_id
            WHERE c.client_id = %s
        """
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO clients (last_name, first_name, middle_name, phone, card_id) VALUES (%s, %s, %s, %s, %s) RETURNING client_id"
        params = (data['last_name'], data['first_name'], data.get('middle_name'), data.get('phone'), data.get('card_id'))
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE clients SET last_name = %s, first_name = %s, middle_name = %s, phone = %s, card_id = %s WHERE client_id = %s RETURNING client_id"
        params = (data['last_name'], data['first_name'], data.get('middle_name'), data.get('phone'), data.get('card_id'), id)
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM clients WHERE client_id = %s"
        execute_query(query, (id,), fetch=False)
        return True