from utils.database import execute_query

class RecipeRepository:
    def find_all(self):
        query = """
            SELECT r.recipe_id, 
                   r.dish_id, 
                   d.name as dish_name,
                   r.ingredient_id, 
                   i.name as ingredient_name,
                   r.portion_weight
            FROM recipes r
            LEFT JOIN dishes d ON r.dish_id = d.dish_id
            LEFT JOIN ingredients i ON r.ingredient_id = i.ingredient_id
            ORDER BY r.recipe_id DESC
        """
        return execute_query(query, fetch=True)

    def insert(self, data):
        query = """
            INSERT INTO recipes (dish_id, ingredient_id, portion_weight) 
            VALUES (%s, %s, %s) 
            RETURNING recipe_id, dish_id, ingredient_id, portion_weight
        """
        params = (
            data['dish_id'], 
            data['ingredient_id'], 
            data['portion_weight']
        )
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def update(self, id, data):
        query = """
            UPDATE recipes 
            SET dish_id = %s, 
                ingredient_id = %s, 
                portion_weight = %s 
            WHERE recipe_id = %s 
            RETURNING recipe_id, dish_id, ingredient_id, portion_weight
        """
        params = (
            data['dish_id'], 
            data['ingredient_id'], 
            data['portion_weight'],
            id
        )
        results = execute_query(query, params, fetch=True)
        return results[0] if results else None

    def delete(self, id):
        query = "DELETE FROM recipes WHERE recipe_id = %s"
        execute_query(query, (id,), fetch=False)
        return True