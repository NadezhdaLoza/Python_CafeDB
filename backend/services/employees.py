from repositories.employees import EmployeeRepository
from utils.error_handler import ErrorHandler

class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        employee = self.repository.find_one(valid_id)
        if not employee:
            raise ValueError("Сотрудник не найден")
        return employee
    
    def create(self, data):
        self.error_handler.validate_required_fields(data, ["last_name", "first_name", "position_id"])
        self.error_handler.validate_string_field(data["last_name"], "last_name")
        self.error_handler.validate_string_field(data["first_name"], "first_name")
        self.error_handler.validate_id(data["position_id"])
        
        clean_data = {
            "last_name": data["last_name"].strip(),
            "first_name": data["first_name"].strip(),
            "middle_name": data.get("middle_name"),
            "phone": data.get("phone"),
            "position_id": data["position_id"]
        }
        result = self.repository.insert(clean_data)
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id", "last_name", "first_name"])
        if data.get("position_id") is None or data.get("position_id") == "":
             raise ValueError("Должность обязательна")
        
        valid_id = self.error_handler.validate_id(data["id"])
        
        last_name = data.get("last_name", "").strip()
        first_name = data.get("first_name", "").strip()
        
        if not last_name or not first_name:
            raise ValueError("Фамилия и Имя обязательны")

        pos_id = data.get("position_id")
        if pos_id:
            try:
                pos_id = int(pos_id)
            except ValueError:
                raise ValueError("Неверный формат ID должности")
        else:
            pos_id = None

        clean_data = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": data.get("middle_name", "").strip(),
            "phone": data.get("phone", "").strip(),
            "position_id": pos_id
        }
        
        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить сотрудника")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}