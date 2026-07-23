from flask import Flask, request, render_template
from phonebook import PhoneBook

app = Flask(__name__)
phonebook = PhoneBook()
phonebook.load()


@app.route('/')
def index():
    return render_template('index.html', contacts=phonebook.contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        name = request.form["name"]
        phone = request.form["phone"]
        phonebook.add(name, phone)
        return render_template('success.html', operation="Добавление")
    return render_template('form.html', big_word='Новый', mode='add')

@app.route('/delete/<name>')
def delete_route(name):
    phonebook.delete(name)
    return render_template('success.html', operation='Удаление')

@app.route('/edit/<name>', methods=['GET','POST'])
def edit_route(name):
    if request.method == 'POST':
        phone = request.form['phone']
        phonebook.edit(name, phone)
        return render_template('success.html', operation='Редактирование')
    contact = phonebook.find(name)
    return render_template('form.html', big_word='Редактировать', mode='edit', current_phone=contact.phone)
    

if __name__ == '__main__':
    app.run()
