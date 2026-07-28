from phonebook import Contact, db
from flask import jsonify, Blueprint, request
from flask_login import login_required, current_user
from datetime import datetime

api_bp = Blueprint('api', __name__)

@api_bp.route('/contacts', methods=['GET'])
@login_required
def api_get_all_contacts():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    result = [
        {
            'id': c.id,
            'name': c.name,
            'phone': c.phone,
            'company': c.company if c.company else None,
            'group': c.group.name if c.group else None
        }
        for c in contacts
    ]
    return jsonify(result)

@api_bp.route('/contacts/<int:contact_id>')
@login_required
def api_get_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id, user_id=current_user.id).first()
    if not contact:
        return jsonify({"error": "Контакт не найден"}), 404
    return jsonify({
        'name': contact.name,
        'phone': contact.phone,
        'company': contact.company if contact.company else None,
        'group': contact.group.name if contact.group else None
    })

@api_bp.route('/contacts', methods=['POST'])
@login_required
def api_add_contact():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    company = data.get('company', '')
    group = data.get('group', None)

    if not name or not phone:
        return jsonify({'error': 'phone and name are required'}), 400
    if not Contact.is_valid_phone(phone):
        return jsonify({'error': 'phone format is invalid'}), 400

    new_contact = Contact(name=name, phone=phone, company=company, user_id=current_user.id, updated_on=datetime.now().strftime('%d.%m.%Y %H:%M'), group_id=group)
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'id': new_contact.id, 'name': new_contact.name}), 201

@api_bp.route('/contacts/<int:contact_id>', methods=['PUT'])
@login_required
def api_edit_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id, user_id=current_user.id).first()
    data = request.get_json()
    new_name = data.get('name')
    new_phone = data.get('phone')
    new_company = data.get('company', '')
    new_group = data.get('group', None)

    if not contact:
        return jsonify({"error": "Контакт не найден"}), 404

    if not new_name or not new_phone:
        return jsonify({'error': 'phone and name are required'}), 400
    if not Contact.is_valid_phone(new_phone):
        return jsonify({'error': 'phone format is invalid'}), 400

    contact.name = new_name
    contact.phone = new_phone
    contact.company = new_company
    contact.updated_on = datetime.now().strftime('%d.%m.%Y %H:%M')
    contact.group_id = new_group
    db.session.commit()
    return jsonify({'message': 'edited successfully'})

@api_bp.route('/contacts/<int:contact_id>', methods=['DELETE'])
@login_required
def api_delete_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id, user_id=current_user.id).first()
    if not contact:
        return jsonify({"error": "Контакт не найден"}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': f'contact {contact_id} deleted'}), 200

    