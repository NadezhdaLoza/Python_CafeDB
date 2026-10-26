from repositories.positions import PositionRepository
from utils.error_handler import ErrorHandler

class PositionService:
    def __init__(self):
        self.repository = PositionRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        position = self.repository.find_one(valid_id)

        if not position:
            raise ValueError("Должность не найдена")
        return position
    
    def create(self, data):
        # 1. Смотрим, что пришло в сервис
        print(f"=== ДАННЫЕ В СЕРВИСЕ CREATE ===")
        print(f"Тип data: {type(data)}")
        print(f"Содержимое data: {data}")
        print(f"Ключи в data: {data.keys() if isinstance(data, dict) else 'Не словарь'}")
        
        # 2. Если data - это не словарь, а например, список или строка, значит проблема во фронтенде/контроллере
        if not isinstance(data, dict):
            raise ValueError(f"Ожидался словарь, получено: {type(data)}")

        # 3. Теперь запускаем валидатор
        self.error_handler.validate_required_fields(data, ["title"])

        clean_data = {
            "title": data["title"].strip()
        }

        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "title"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["title"], "title")
        
        clean_data = {
            "title": data["title"].strip()
        }

        result = self.repository.update(valid_id, clean_data)
        
        if not result:
            raise ValueError("Не удалось обновить должность (возможно, неверный ID)")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}