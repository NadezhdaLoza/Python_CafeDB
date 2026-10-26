from repositories.categories import CategoryRepository
from utils.error_handler import ErrorHandler

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        category = self.repository.find_one(valid_id)
        if not category:
            raise ValueError("Категория не найдена")
        return category
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["title"])
        self.error_handler.validate_string_field(data["title"], "title")
        clean_data = {"title": data["title"].strip()}
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "title"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["title"], "title")
        clean_data = {"title": data["title"].strip()}
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить категорию")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}