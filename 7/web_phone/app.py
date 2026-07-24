# app.py
from flask import Flask
from phonebook import db
from routes import phonebook_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db.init_app(app)
app.register_blueprint(phonebook_bp)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()