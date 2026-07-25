from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from phonebook import PhoneBook, Contact, Group

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
        company = request.form["company"]
        phonebook.add(name, phone, company, current_user.id)
        return render_template('success.html', operation="Добавление")
    return render_template('form.html', big_word='Новый контакт', mode='add', name_label="Имя", submit_text='Добавить контакт')

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
        company = request.form.get("company", "")
        phonebook.edit(name, phone, company, current_user.id)
        return render_template('success.html', operation='Редактирование')
    contact = phonebook.find(name, current_user.id)
    groups = Group.query.filter_by(user_id=current_user.id).all()
    return render_template('form.html', big_word='Изменить контакт', mode='edit', current_phone=contact.phone, current_company=contact.company, groups=groups, submit_text='Изменить контакт')

@phonebook_bp.route('/groups/add', methods=['GET', 'POST'])
@login_required
def add_group_route():
    if request.method == 'POST':
        name = request.form['name']
        phonebook.add_group(name, current_user.id)
        return render_template('success.html', operation='Добавление группы')
    return render_template('form.html', big_word='Новая группа', mode='add_group', name_label="Название", submit_text='Добавить группу')