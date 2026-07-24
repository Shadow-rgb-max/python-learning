from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from phonebook import PhoneBook, Contact

phonebook_bp = Blueprint('phonebook', __name__)
phonebook = PhoneBook()

@phonebook_bp.route('/')
@login_required
def index():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', contacts=contacts)

@phonebook_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_route():
    if request.method == 'POST':
        name = request.form["name"]
        phone = request.form["phone"]
        phonebook.add(name, phone, current_user.id)
        return render_template('success.html', operation="Добавление")
    return render_template('form.html', big_word='Новый', mode='add')

@phonebook_bp.route('/delete/<name>')
@login_required
def delete_route(name):
    phonebook.delete(name, current_user.id)
    return render_template('success.html', operation='Удаление')

@phonebook_bp.route('/edit/<name>', methods=['GET', 'POST'])
@login_required
def edit_route(name):
    if request.method == 'POST':
        phone = request.form['phone']
        phonebook.edit(name, phone, current_user.id)
        return render_template('success.html', operation='Редактирование')
    contact = phonebook.find(name, current_user.id)
    return render_template('form.html', big_word='Редактировать', mode='edit', current_phone=contact.phone)