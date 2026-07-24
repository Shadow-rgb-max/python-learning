from flask import Flask
from phonebook import db
from routes import phonebook_bp
from auth import auth_bp
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from phonebook import User
    return db.session.get(User, int(user_id))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET_KEY'] = 'любая-случайная-строка-держи-в-секрете'
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(phonebook_bp)
app.register_blueprint(auth_bp)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()