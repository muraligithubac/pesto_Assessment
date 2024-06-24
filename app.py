from flask import Flask, request, jsonify
from models import db, User
from routes import auth_bp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/ecommerce_auth')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(auth_bp)

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
