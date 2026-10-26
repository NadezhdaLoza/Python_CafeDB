from utils.database import execute_query

class BonusCardRepository:
    def find_all(self):
        query = "SELECT * FROM bonus_cards ORDER BY issue_date DESC"
        return execute_query(query, fetch=True)

    def find_one(self, id):
        query = "SELECT * FROM bonus_cards WHERE card_id = %s"
        results = execute_query(query, (id,), fetch=True)
        return results[0] if results else None

    def insert(self, data):
        query = """
            INSERT INTO bonus_cards (card_number, balance, issue_date) 
            VALUES (%s, %s, %s) 
            RETURNING card_id, card_number, balance, issue_date
        """
        params = (data['card_number'], data['balance'], data['issue_date'])
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None
        
    def update(self, id, data):
        query = "UPDATE bonus_cards SET card_number = %s, balance = %s, issue_date = %s WHERE card_id = %s RETURNING card_id"
        params = (data.get('card_number'), data.get('balance'), data.get('issue_date'), id)
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM bonus_cards WHERE card_id = %s"
        execute_query(query, (id,), fetch=False)
        return True