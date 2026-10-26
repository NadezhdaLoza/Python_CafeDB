from utils.database import execute_query

class SupplierRepository:
    def find_all(self):
        query = "SELECT * FROM suppliers ORDER BY company_name ASC"
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = "SELECT * FROM suppliers WHERE supplier_id = %s"
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO suppliers (company_name, manager_full_name, phone) VALUES (%s, %s, %s) RETURNING supplier_id"
        params = (data['company_name'], data.get('manager_full_name'), data.get('phone'))
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE suppliers SET company_name = %s, manager_full_name = %s, phone = %s WHERE supplier_id = %s RETURNING supplier_id"
        params = (data['company_name'], data.get('manager_full_name'), data.get('phone'), id)
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM suppliers WHERE supplier_id = %s"
        execute_query(query, (id,), fetch=False)
        return True