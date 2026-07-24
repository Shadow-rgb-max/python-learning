# app.py
from flask import Flask
from phonebook import db
from routes import phonebook_bp
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def load_user(user_id):
    from phonebook import User
    return User.query.get(int(user_id))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db.init_app(app)
app.register_blueprint(phonebook_bp)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()