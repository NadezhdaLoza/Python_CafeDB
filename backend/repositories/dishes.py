from utils.database import execute_query

class DishRepository:
    def find_all(self):
        query = """
            SELECT d.dish_id, 
                   d.name, 
                   d.price, 
                   d.weight, 
                   d.article_number,
                   d.unit,
                   d.category_id,
                   c.title as category_title
            FROM dishes d
            LEFT JOIN categories c ON d.category_id = c.category_id
            ORDER BY d.name ASC
        """
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = """
            SELECT d.dish_id, d.name, d.price, d.weight, d.article_number, d.unit, c.title as category_title
            FROM dishes d
            LEFT JOIN categories c ON d.category_id = c.category_id
            WHERE d.dish_id = %s
        """
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO dishes (name, price, weight, article_number, unit, category_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING dish_id"
        params = (data['name'], data.get('price'), data.get('weight'), data.get('article_number'), data.get('unit'), data.get('category_id'))
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE dishes SET name = %s, price = %s, weight = %s, article_number = %s, unit = %s, category_id = %s WHERE dish_id = %s RETURNING dish_id"
        params = (data['name'], data.get('price'), data.get('weight'), data.get('article_number'), data.get('unit'), data.get('category_id'), id)
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM dishes WHERE dish_id = %s"
        execute_query(query, (id,), fetch=False)
        return True