from repositories.orders import OrderRepository
from utils.error_handler import ErrorHandler

class OrderService:
    def __init__(self):
        self.repository = OrderRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        try:
            print("Сервис запрашивает все заказы...")
            return self.repository.find_all()
        except Exception as e:
            print(f"!!! ОШИБКА В СЕРВИСЕ ORDERS GET_ALL: {e}")
            import traceback
            traceback.print_exc()
            raise e
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        order = self.repository.find_one(valid_id)
        
        if not order:
            raise ValueError("Заказ не найден")
        return order
    
    def create(self, data):
        print(f"Данные заказа на бэкенде: {data}")

        if not data.get('order_number'):
            raise ValueError("Номер заказа обязателен")
        if not data.get('client_id'):
            raise ValueError("Клиент обязателен")
        if not data.get('employee_id'):
            raise ValueError("Сотрудник обязателен")
        if not data.get('order_date'):
            raise ValueError("Дата обязательна")

        order_header = {
            "order_number": int(data['order_number']),
            "order_date": data['order_date'],
            "order_time": data.get('order_time', '12:00:00'),
            "client_id": int(data['client_id']),
            "employee_id": int(data['employee_id']),
            "total_amount": float(data.get('total_amount', 0))
        }

        items_list = []
        items_from_form = data.get('items', [])
        
        for item in items_from_form:
            if not item.get('dish_id'):
                continue

            items_list.append({
                "dish_id": int(item['dish_id']),
                "quantity": int(item['quantity']),
                "price": float(item['price']),
                "total_amount": float(item['total_amount']),
                "article_number": item.get('article_number'),
                "unit": item.get('unit')                   
            })

        result = self.repository.insert(order_header, items_list)
        
        if not result:
            raise ValueError("Не удалось создать заказ")
            
        return result

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id"])
        valid_id = self.error_handler.validate_id(data["id"])

        # Валидация полей шапки
        self.error_handler.validate_required_fields(data, [
            "order_number", "employee_id", "client_id", 
            "order_date", "total_amount"
        ])
        
        order_header = {
            "order_number": data["order_number"],
            "employee_id": data["employee_id"],
            "client_id": data["client_id"],
            "order_date": data["order_date"],
            "order_time": data.get("order_time", "12:00:00"),
            "total_amount": data["total_amount"]
        }

        items_list = data.get("items", [])
        
        result = self.repository.update(valid_id, order_header, items_list)
        
        if not result:
            raise ValueError("Заказ не найден или не обновлен")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}