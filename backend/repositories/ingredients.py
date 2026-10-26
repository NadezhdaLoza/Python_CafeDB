from utils.database import execute_query

class IngredientRepository:
    def find_all(self):
        query = """
            SELECT i.ingredient_id, 
                   i.name, 
                   i.unit, 
                   i.supplier_id,
                   s.company_name as supplier_name -- Опционально: название поставщика для отображения
            FROM ingredients i
            LEFT JOIN suppliers s ON i.supplier_id = s.supplier_id
            ORDER BY i.name ASC
        """
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = """
            SELECT i.ingredient_id, i.name, i.unit, s.company_name as supplier_name
            FROM ingredients i
            LEFT JOIN suppliers s ON i.supplier_id = s.supplier_id
            WHERE i.ingredient_id = %s
        """
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO ingredients (name, unit, supplier_id) VALUES (%s, %s, %s) RETURNING ingredient_id"
        params = (data['name'], data.get('unit'), data.get('supplier_id'))
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE ingredients SET name = %s, unit = %s, supplier_id = %s WHERE ingredient_id = %s RETURNING ingredient_id"
        params = (data['name'], data.get('unit'), data.get('supplier_id'), id)
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM ingredients WHERE ingredient_id = %s"
        execute_query(query, (id,), fetch=False)
        return True