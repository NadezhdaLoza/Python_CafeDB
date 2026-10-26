from repositories.ingredients import IngredientRepository
from utils.error_handler import ErrorHandler

class IngredientService:
    def __init__(self):
        self.repository = IngredientRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        ingredient = self.repository.find_one(valid_id)
        if not ingredient:
            raise ValueError("Ингредиент не найден")
        return ingredient
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["name"])
        self.error_handler.validate_string_field(data["name"], "name")
        clean_data = {
            "name": data["name"].strip(),
            "unit": data.get("unit"),
            "supplier_id": data.get("supplier_id")
        }
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "name"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["name"], "name")
        clean_data = {
            "name": data["name"].strip(),
            "unit": data.get("unit"),
            "supplier_id": data.get("supplier_id")
        }
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить ингредиент")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}