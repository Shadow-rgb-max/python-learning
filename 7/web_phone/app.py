from flask import Flask, redirect, url_for
from phonebook import db
from routes import phonebook_bp
from auth import auth_bp
from api import api_bp
from flask_login import LoginManager
from flask_migrate import Migrate

migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET_KEY'] = 'любая-случайная-строка-держи-в-секрете'
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from phonebook import User
    return db.session.get(User, int(user_id))

@app.route('/')
def redirect_to_contacts():
    return redirect(url_for('phonebook.index'))

app.register_blueprint(phonebook_bp, url_prefix='/contacts')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()