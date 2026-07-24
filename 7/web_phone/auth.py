from flask import Blueprint, url_for, redirect, request, render_template
from flask_login import login_user, logout_user, login_required
from phonebook import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass