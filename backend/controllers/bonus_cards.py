from flask import jsonify, request
from services.bonus_cards import BonusCardService

class BonusCardController:
    def __init__(self):
        self.service = BonusCardService()

    def get_all(self):
        try:
            return jsonify(self.service.get_all())
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 400
        except Exception as error:
            return jsonify({"success": False, "error": str(error)}), 500
    
    def get_one(self, id):
        try:
            return jsonify(self.service.get_one(id))
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 400
        except Exception as error:
            return jsonify({"success": False, "error": str(error)}), 500
    
    def post(self):
        try:
            data = request.get_json()
            print(f"=== БОНУСНЫЕ КАРТЫ: ПОЛУЧЕНЫ ДАННЫЕ ===")
            print(f"Данные: {data}")
            
            result = self.service.create(data)
            return jsonify(result), 201
        except Exception as e:
            print(f"!!! ОШИБКА ПРИ СОЗДАНИИ КАРТЫ: {str(e)}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": str(e), "success": False}), 400
    
    def put(self):
        try:
            data = request.get_json()
            return jsonify(self.service.update(data))
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 400
        except Exception as error:
            return jsonify({"success": False, "error": str(error)}), 500

    def delete(self, id):
        try:
            return jsonify(self.service.delete(id))
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 400
        except Exception as error:
            return jsonify({"success": False, "error": str(error)}), 500