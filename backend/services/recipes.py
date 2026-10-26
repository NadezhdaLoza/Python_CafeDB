from repositories.recipes import RecipeRepository
from utils.error_handler import ErrorHandler

class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["dish_id", "ingredient_id", "portion_weight"])
        
        try:
            portion_weight = float(data['portion_weight'])
        except ValueError:
            raise ValueError("Вес порции должен быть числом")
            
        clean_data = {
            "dish_id": int(data['dish_id']),
            "ingredient_id": int(data['ingredient_id']),
            "portion_weight": portion_weight
        }
        
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "dish_id", "ingredient_id", "portion_weight"])
        valid_id = self.error_handler.validate_id(data["id"])
        
        try:
            portion_weight = float(data['portion_weight'])
        except ValueError:
            raise ValueError("Вес порции должен быть числом")

        clean_data = {
            "dish_id": int(data['dish_id']),
            "ingredient_id": int(data['ingredient_id']),
            "portion_weight": portion_weight
        }
        
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить рецепт")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}