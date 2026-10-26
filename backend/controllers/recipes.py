from flask import jsonify, request
from services.recipes import RecipeService

class RecipeController:
    def __init__(self):
        self.service = RecipeService()

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