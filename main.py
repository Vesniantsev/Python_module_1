contacts = [
    {"name": "Анднеев Андрей", "phone": "111111111111", "mail": "andrey@mail.com"},
    {"name": "Борисов Борис", "phone": "222222222222", "mail": "borya@mail.com"},
    {"name": "Витальев Виталий", "phone": "333333333333", "mail": "vitalik@mail.com"},
    {"name": "Григорьев Григорий", "phone": "444444444444", "mail": "grigoriy@mail.com"},
    {"name": "Дмитриев Дмитрий", "phone": "555555555555", "mail": "dima@mail.com"},
    {"name": "Жириновский Жак", "phone": "666666666666", "mail": "zak@mail.com"},
    {"name": "Ельцин Евгений", "phone": "777777777777", "mail": "evgen@mail.com"},
    {"name": "Кучма Кирил", "phone": "888888888888", "mail": "kiril@mail.com"},
    {"name": "Трамп Тимофей", "phone": "999999999999", "mail": "tramp@mail.com"}
]

with open("contacts.txt", "w") as file:
    for contact in contacts:
        file.write(f"Имя: {contact['name']}, телефон: {contact['phone']}, mail: {contact['mail']}\n")
print("✅ Контакты успешно записаны в файл contacts.txt!")

def input_name():
    while True:  
        name = input("Введите имя: ")
        if name == "":  
            print("❌ Имя не может быть пустым.")
        else:
            print("✅ Имя принято!")
            return name 

def input_phone():
    while True:
        phone = input("Введите телефон (12 цифр): ")
        
        if not phone.isdigit():
            print("❌ Телефон должен содержать только цифры.")
        elif len(phone) != 12:
            print("❌ Телефон должен содержать ровно 12 цифр.")
        else:
            print("✅ Телефон принят!")
            return phone  

def input_email():
    while True:
        email = input("Введите email: ")

        if '@' not in email or '.' not in email:
            print("❌ Email должен содержать символы '@' и '.'.")
        else:
            print("✅ Email принят!")
            return email

def add_contact():
    name = input_name()
    phone = input_phone()
    email = input_email()
    contact_new = f"Имя: {name}, телефон: {phone}, mail: {email}\n"
    with open("contacts.txt", "a") as file:
        file.write(contact_new) 
    print("✅ Контакт успешно добавлен!")
    return contact_new
add_contact()

def load_contacts():
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    contacts = []
    for line in lines:
        parts = line.split(", ")
        contact = {}
        for part in parts:
            key_value = part.split(": ")
            if len(key_value) == 2:
                key, value = key_value
                contact[key] = value
        contacts.append(contact)
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"Имя: {contact['Имя']}, телефон: {contact['телефон']}, mail: {contact['mail']}\n")

def search_contact():
    contacts = load_contacts()
    search = input("Введите имя или телефон для поиска: ")
    found = False
    for contact in contacts:
        if search in contact["Имя"] or search in contact["телефон"]:
            print(f"Найден: {contact['Имя']}, {contact['телефон']}, {contact['mail']}")
            found = True
    if not found:
        print("❌ Контакт не найден.")

def delete_contact():
    contacts = load_contacts()
    search = input("Введите имя или телефон для удаления: ")
    new_contacts = []
    found = False
    for contact in contacts:
        if search in contact["Имя"] or search in contact["телефон"]:
            found = True
        else:
            new_contacts.append(contact)
    if found:
        save_contacts(new_contacts)
        print("✅ Контакт удалён!")
    else:
        print("❌ Контакт не найден.")

def update_contact():
    contacts = load_contacts()
    search = input("Введите имя или телефон для обновления: ")
    updated = False
    for i in range(len(contacts)):
        if search in contacts[i]["Имя"] or search in contacts[i]["телефон"]:
            print("Введите новые данные:")
            name = input_name()
            phone = input_phone()
            email = input_email()
            contacts[i] = {"Имя": name, "телефон": phone, "mail": email}
            updated = True
            break
    if updated:
        save_contacts(contacts)
        print("✅ Контакт обновлён!")
    else:
        print("❌ Контакт не найден.")

def view_contacts():
    contacts = load_contacts()
    contacts.sort(key=lambda x: x["Имя"])
    print("Все контакты:")
    for contact in contacts:
        print(f"{contact['Имя']} | {contact['телефон']} | {contact['mail']}")

def show_menu():
    print("\nВыберите действие:")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Посмотреть контакты")
    print("6. Выйти")

while True:
    show_menu()
    choice = input("Ваш выбор: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        view_contacts()
    elif choice == "6":
        print("Программа завершена. До свидания!")
        break
    else:
        print("❌ Неверный выбор. Попробуйте снова.")



