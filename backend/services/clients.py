from repositories.clients import ClientRepository
from utils.error_handler import ErrorHandler

class ClientService:
    def __init__(self):
        self.repository = ClientRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        client = self.repository.find_one(valid_id)
        if not client:
            raise ValueError("Клиент не найден")
        return client
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["last_name", "first_name"])
        self.error_handler.validate_string_field(data["last_name"], "last_name")
        self.error_handler.validate_string_field(data["first_name"], "first_name")
        
        clean_data = {
            "last_name": data["last_name"].strip(),
            "first_name": data["first_name"].strip(),
            "middle_name": data.get("middle_name"),
            "phone": data.get("phone"),
            "card_id": data.get("card_id")
        }
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "last_name", "first_name"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["last_name"], "last_name")
        self.error_handler.validate_string_field(data["first_name"], "first_name")
        
        clean_data = {
            "last_name": data["last_name"].strip(),
            "first_name": data["first_name"].strip(),
            "middle_name": data.get("middle_name"),
            "phone": data.get("phone"),
            "card_id": data.get("card_id")
        }
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить клиента")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}