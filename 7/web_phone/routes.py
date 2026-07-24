from flask import Blueprint, request, render_template
from phonebook import PhoneBook, Contact

phonebook_bp = Blueprint('phonebook', __name__)
phonebook = PhoneBook()

@phonebook_bp.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@phonebook_bp.route('/add', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        name = request.form["name"]
        phone = request.form["phone"]
        phonebook.add(name, phone)
        return render_template('success.html', operation="Добавление")
    return render_template('form.html', big_word='Новый', mode='add')

@phonebook_bp.route('/delete/<name>')
def delete_route(name):
    phonebook.delete(name)
    return render_template('success.html', operation='Удаление')

@phonebook_bp.route('/edit/<name>', methods=['GET', 'POST'])
def edit_route(name):
    if request.method == 'POST':
        phone = request.form['phone']
        phonebook.edit(name, phone)
        return render_template('success.html', operation='Редактирование')
    contact = phonebook.find(name)
    return render_template('form.html', big_word='Редактировать', mode='edit', current_phone=contact.phone)