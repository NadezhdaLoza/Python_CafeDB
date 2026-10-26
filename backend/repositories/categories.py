from utils.database import execute_query

class CategoryRepository:
    def find_all(self):
        query = "SELECT * FROM categories ORDER BY title ASC"
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = "SELECT * FROM categories WHERE category_id = %s"
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO categories (title) VALUES (%s) RETURNING category_id, title"
        results = execute_query(query, (data['title'],), fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE categories SET title = %s WHERE category_id = %s RETURNING category_id, title"
        results = execute_query(query, (data['title'], id), fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM categories WHERE category_id = %s"
        execute_query(query, (id,), fetch=False)
        return True