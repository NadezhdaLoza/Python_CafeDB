from repositories.dishes import DishRepository
from repositories.recipes import RecipeRepository
from utils.error_handler import ErrorHandler

class DishService:
    def __init__(self):
        self.repository = DishRepository()
        self.recipe_repository = RecipeRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        dish = self.repository.find_one(valid_id)
        if not dish:
            raise ValueError("Блюдо не найдено")
        return dish
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["name", "price"])
        self.error_handler.validate_string_field(data["name"], "name")
        self.error_handler.validate_int_field(data["price"], "price")
        
        clean_data = {
            "name": data["name"].strip(),
            "price": data["price"],
            "weight": data.get("weight"),
            "article_number": data.get("article_number"),
            "unit": data.get("unit"),
            "category_id": data.get("category_id")
        }
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "name", "price"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["name"], "name")
        self.error_handler.validate_int_field(data["price"], "price")
        
        clean_data = {
            "name": data["name"].strip(),
            "price": data["price"],
            "weight": data.get("weight"),
            "article_number": data.get("article_number"),
            "unit": data.get("unit"),
            "category_id": data.get("category_id")
        }
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить блюдо")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.recipe_repository.delete_by_dish(valid_id)
        self.repository.delete(valid_id)
        return {"success": True}