from flask import jsonify, request
from services.orders import OrderService

class OrderController:
    def __init__(self):
        self.service = OrderService()

    def get_all(self):
        try:
            orders = self.service.get_all()

            clean_orders = []
            for order in orders:
                clean_order = {}
                for key, value in order.items():
                    if hasattr(value, '__float__'): 
                        clean_order[key] = float(value)

                    elif hasattr(value, 'isoformat'):
                        clean_order[key] = value.isoformat()
                    else:
                        clean_order[key] = value
                clean_orders.append(clean_order)
                
            return jsonify(clean_orders), 200
            
        except Exception as e:
            print(f"Ошибка в контроллере при сериализации заказов: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": "Ошибка сервера при обработке данных"}), 500
    
    def get_one(self, id):
        try:
            order = self.service.get_one(id)

            clean_order = {}
            for key, value in order.items():
                if key == 'items':
                    clean_items = []
                    for item in value:
                        clean_item = {}
                        for k, v in item.items():
                            if hasattr(v, '__float__') and not isinstance(v, bool):
                                clean_item[k] = float(v)
                            elif hasattr(v, 'isoformat'):
                                clean_item[k] = v.isoformat()
                            else:
                                clean_item[k] = v
                        clean_items.append(clean_item)
                    clean_order[key] = clean_items
                else:
                    if hasattr(value, '__float__') and not isinstance(value, bool):
                        clean_order[key] = float(value)
                    elif hasattr(value, 'isoformat'):
                        clean_order[key] = value.isoformat()
                    else:
                        clean_order[key] = value
                        
            return jsonify(clean_order), 200
            
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 404
        except Exception as error:
            print(f"Ошибка в контроллере get_one: {error}")
            import traceback
            traceback.print_exc()
            return jsonify({"success": False, "error": "Ошибка сервера"}), 500
    
    def post(self):
        try:
            data = request.get_json()
            return jsonify(self.service.create(data)), 201
        except ValueError as error:
            return jsonify({"success": False, "error": str(error)}), 400
        except Exception as error:
            return jsonify({"success": False, "error": str(error)}), 500
    
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