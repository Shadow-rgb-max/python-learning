from phonebook import Phonebook

def test_add_contact():
    pb = Phonebook()
    assert pb.add("Иван Иванов", "7-123-456-78-90") == True
    assert pb.add("Иван Иванов", "7-123-456-78-90") == False  # Duplicate contact

def test_delete_contact():
    pb = Phonebook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    assert pb.delete("Иван Иванов") == True
    assert pb.delete("Иван Иванов") == False  # Contact already deleted

def test_edit_contact():
    pb = Phonebook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    assert pb.edit("Иван Иванов", "7-987-654-32-10") == True
    assert pb.edit("Петр Петров", "7-987-654-32-10") == False  # Contact does not exist

def test_invalid_phone_format():
    pb = Phonebook()
    try:
        pb.add("Иван Иванов", "1234567890")  # Invalid format
    except ValueError as e:
        assert str(e) == "Неверный формат номера телефона."

def test_valid_phone_format():
    assert Phonebook.is_valid_phone("7-123-456-78-90") == True
    assert Phonebook.is_valid_phone("1234567890") == False

def test_save_and_load():
    pb = Phonebook()
    pb.add("Иван Иванов", "7-123-456-78-90")
    pb.save("test_contacts.json")
    
    pb2 = Phonebook()
    pb2.load("test_contacts.json")
    assert "Иван Иванов" in pb2.contacts
    assert pb2.contacts["Иван Иванов"].phone == "7-123-456-78-90"

def test_contact_str():
    contact = Phonebook.Contact("Иван Иванов", "7-123-456-78-90", "2024-01-01T12:00:00")
    assert str(contact) == "Имя: Иван Иванов, Номер телефона: 7-123-456-78-90, Последнее обновление: 2024-01-01T12:00:00"

