from flask import Flask
from flask_cors import CORS
from routes.routes import router
from utils.json_encoder import CustomJSONEncoder

def create_app():
    app = Flask(__name__)
    
    CORS(app, 
     origins=["http://localhost:8090", "http://127.0.0.1:8090"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=True)
    
    app.json = CustomJSONEncoder(app)
    app.register_blueprint(router)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
