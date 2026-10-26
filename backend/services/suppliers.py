from repositories.suppliers import SupplierRepository
from utils.error_handler import ErrorHandler

class SupplierService:
    def __init__(self):
        self.repository = SupplierRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        supplier = self.repository.find_one(valid_id)
        if not supplier:
            raise ValueError("Поставщик не найден")
        return supplier
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["company_name"])
        self.error_handler.validate_string_field(data["company_name"], "company_name")
        clean_data = {
            "company_name": data["company_name"].strip(),
            "manager_full_name": data.get("manager_full_name"),
            "phone": data.get("phone")
        }
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "company_name"])
        valid_id = self.error_handler.validate_id(data["id"])
        self.error_handler.validate_string_field(data["company_name"], "company_name")
        clean_data = {
            "company_name": data["company_name"].strip(),
            "manager_full_name": data.get("manager_full_name"),
            "phone": data.get("phone")
        }
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить поставщика")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}