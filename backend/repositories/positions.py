from utils.database import execute_query

class PositionRepository:
    def find_all(self):
        query = "SELECT * FROM positions ORDER BY title ASC"
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = "SELECT * FROM positions WHERE position_id = %s"
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = "INSERT INTO positions (title) VALUES (%s) RETURNING position_id, title"
        results = execute_query(query, (data['title'],), fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = "UPDATE positions SET title = %s WHERE position_id = %s RETURNING position_id, title"
        results = execute_query(query, (data['title'], id), fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM positions WHERE position_id = %s"
        execute_query(query, (id,), fetch=False)
        return True