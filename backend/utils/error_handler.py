from datetime import datetime

class ErrorHandler:
    
    @staticmethod
    def validate_id(id_value):
        if id_value is None:
            raise ValueError("ID не может быть пустым")
        try:
            id_int = int(id_value)
        except (ValueError, TypeError):
            raise ValueError("ID должен быть целым числом")
        if id_int <= 0:
            raise ValueError("ID должен быть положительным числом")
        return id_int

    @staticmethod
    def validate_string_field(value, field_name):
        if value is None:
            raise ValueError(f"Поле '{field_name}' не может быть None")
        if not isinstance(value, str):
            raise ValueError(f"Поле '{field_name}' должно быть строкой")
        if not value.strip():
            raise ValueError(f"Поле '{field_name}' не может быть пустым")

    @staticmethod
    def validate_int_field(value, field_name, min_val=0):
        if value is None:
            raise ValueError(f"Поле '{field_name}' не может быть None")
        try:
            num_val = int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Поле '{field_name}' должно быть целым числом")
        if num_val < min_val:
            raise ValueError(f"Поле '{field_name}' не может быть меньше {min_val}")
        return num_val

    @staticmethod
    def validate_date_format(date_str, field_name="Дата"):
        if not isinstance(date_str, str):
            raise ValueError(f"{field_name} должна быть строкой")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"{field_name} имеет неверный формат. Ожидается YYYY-MM-DD")

    @staticmethod
    def validate_required_fields(data, fields):
        for field in fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
            
            value = data[field]

            if isinstance(value, str) and not value.strip():
                 raise ValueError(f"Поле '{field}' не может быть пустой строкой")