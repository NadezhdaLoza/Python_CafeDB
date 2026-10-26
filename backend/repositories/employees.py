from utils.database import execute_query

class EmployeeRepository:
    def find_all(self):
        query = """
            SELECT e.employee_id, e.last_name, e.first_name, e.middle_name,
                   e.last_name || ' ' || e.first_name || ' ' || COALESCE(e.middle_name, '') as full_name,
                   e.phone,
                   p.position_id,
                   p.title as position_title
            FROM employees e
            LEFT JOIN positions p ON e.position_id = p.position_id
            ORDER BY e.last_name ASC
        """
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = """
            SELECT e.employee_id, e.last_name, e.first_name, e.middle_name, e.phone, 
                   p.title as position_title
            FROM employees e
            LEFT JOIN positions p ON e.position_id = p.position_id
            WHERE e.employee_id = %s
        """
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO employees (last_name, first_name, middle_name, phone, position_id) VALUES (%s, %s, %s, %s, %s) RETURNING employee_id"
        params = (data['last_name'], data['first_name'], data.get('middle_name'), data.get('phone'), data.get('position_id'))
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = """
            UPDATE employees 
            SET last_name = %s, 
                first_name = %s, 
                middle_name = %s, 
                phone = %s, 
                position_id = %s 
            WHERE employee_id = %s 
            RETURNING employee_id, last_name, first_name, middle_name, phone, position_id
        """
        params = (
            data['last_name'],
            data['first_name'],
            data.get('middle_name'),
            data.get('phone'), 
            data.get('position_id'),
            id
        )
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM employees WHERE employee_id = %s"
        execute_query(query, (id,), fetch=False)
        return True