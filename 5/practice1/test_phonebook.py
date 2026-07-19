from phonebook import PhoneBook, Contact
import pytest

def test_add_contact():
    pb = PhoneBook()
    assert pb.add("Иван Иванов", "7-123-456-78-90") == True
    assert pb.add("Иван Иванов", "7-123-456-78-90") == False  # Duplicate contact

def test_delete_contact():
    pb = PhoneBook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    assert pb.delete("Иван Иванов") == True
    assert pb.delete("Иван Иванов") == False  # Contact already deleted

def test_edit_contact():
    pb = PhoneBook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    assert pb.edit("Иван Иванов", "7-987-654-32-10") == True
    assert pb.edit("Петр Петров", "7-987-654-32-10") == False  # Contact does not exist

def test_invalid_phone_format():
    pb = PhoneBook()
    with pytest.raises(ValueError, match="Неверный формат номера телефона.") as e:
        pb.add("Иван Иванов", "1234567890")  # Invalid format

def test_valid_phone_format():
    assert Contact.is_valid_phone("7-123-456-78-90") == True
    assert Contact.is_valid_phone("1234567890") == False

def test_save_and_load():
    pb = PhoneBook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    pb.save("test_contacts.json")
    
    pb2 = PhoneBook()
    pb2.load("test_contacts.json")
    assert "Иван Иванов" in pb2.contacts
    assert pb2.contacts["Иван Иванов"].phone == "7-123-456-78-90"

def test_contact_str():
    contact = Contact("Иван Иванов", "7-123-456-78-90", "2024-01-01T12:00:00")
    assert str(contact) == "Имя: Иван Иванов, Номер телефона: 7-123-456-78-90, Последнее обновление: 2024-01-01T12:00:00"

