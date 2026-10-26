from repositories.bonus_cards import BonusCardRepository
from utils.error_handler import ErrorHandler

class BonusCardService:
    def __init__(self):
        self.repository = BonusCardRepository()
        self.error_handler = ErrorHandler()

    def get_all(self):
        return self.repository.find_all()
    
    def get_one(self, id):
        valid_id = self.error_handler.validate_id(id)
        card = self.repository.find_one(valid_id)
        if not card:
            raise ValueError("Карта не найдена")
        return card
    
    def create(self, data):
        print(f"Сервис получил: {data}")
        
        # Временная простая проверка
        card_number = data.get("card_number")
        if not card_number:
            raise ValueError("Номер карты обязателен")

        balance = data.get("balance", 0)
        # Преобразуем баланс в число, если он пришел строкой
        try:
            balance = int(balance) if balance is not None else 0
        except ValueError:
            raise ValueError("Баланс должен быть числом")

        issue_date = data.get("issue_date")
        if issue_date == "":
            issue_date = None

        clean_data = {
            "card_number": str(card_number).strip(),
            "balance": balance,
            "issue_date": issue_date
        }
        
        print(f"Отправляем в репозиторий: {clean_data}")
        return self.repository.insert(clean_data)

    def update(self, data):
        self.error_handler.validate_required_fields(data, ["id"])
        valid_id = self.error_handler.validate_id(data["id"])
        
        balance = data.get("balance")
        if balance is not None and balance != "":
            try:
                balance = int(balance)
            except ValueError:
                raise ValueError("Баланс должен быть числом")
        else:
            balance = 0

        issue_date = data.get("issue_date")
        if not issue_date:
            issue_date = None

        clean_data = {
            "card_number": data.get("card_number"),
            "balance": balance,
            "issue_date": issue_date
        }
        
        if not clean_data["card_number"]:
             pass 

        result = self.repository.update(valid_id, clean_data)
        if not result:
            raise ValueError("Не удалось обновить карту")
        return result

    def delete(self, id):
        valid_id = self.error_handler.validate_id(id)
        self.repository.delete(valid_id)
        return {"success": True}