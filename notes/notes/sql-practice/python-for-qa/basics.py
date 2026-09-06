# ============================================
# PYTHON ДЛЯ QA ИНЖЕНЕРА
# ============================================

# 1. БАЗОВЫЙ СИНТАКСИС
# ============================================

# Переменные
name = "Ivan"
age = 19
is_student = True

# 2. РАБОТА СО СТРОКАМИ
# ============================================

text = "Hello, World!"

# Методы строк
print(text.lower())           # hello, world!
print(text.upper())           # HELLO, WORLD!
print(text.replace("H", "J")) # Jello, World!
print(text.split(", "))       # ['Hello', 'World!']
print(len(text))              # 13

# 3. ЧИСЛА И ОПЕРАЦИИ
# ============================================

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (целочисленное деление)
print(a % b)   # 1 (остаток)
print(a ** b)  # 1000 (степень)

# 4. СПИСКИ
# ============================================

numbers = [1, 2, 3, 4, 5]
names = ["Ivan", "Maria", "Petr"]

# Доступ к элементам
print(numbers[0])      # 1
print(names[-1])       # последний элемент

# Методы списков
numbers.append(6)      # добавить в конец
numbers.insert(0, 0)   # вставить на позицию
numbers.remove(3)      # удалить элемент
numbers.pop()          # удалить последний
len(numbers)           # длина списка

# Срезы
print(numbers[1:3])    # [2, 3]
print(numbers[:3])     # первые 3
print(numbers[3:])     # с 3 до конца

# 5. УСЛОВИЯ (if/elif/else)
# ============================================

age = 20

if age < 18:
    print("Несовершеннолетний")
elif age < 60:
    print("Взрослый")
else:
    print("Пенсионер")

# 6. ЦИКЛЫ
# ============================================

# for
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# for с списком
names = ["Ivan", "Maria", "Petr"]
for name in names:
    print(name)

# while
count = 0
while count < 5:
    print(count)
    count += 1

# 7. ФУНКЦИИ
# ============================================

def greet(name):
    """Приветствие пользователя"""
    return f"Hello, {name}!"

print(greet("Ivan"))  # Hello, Ivan!

def calculate_sum(a, b):
    """Сложение двух чисел"""
    return a + b

result = calculate_sum(5, 3)
print(result)  # 8

# 8. РАБОТА С ФАЙЛАМИ
# ============================================

# Чтение файла
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Запись в файл
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!")

# 9. ASSERT (ПРОВЕРКИ)
# ============================================

# Простые проверки
assert 2 + 2 == 4
assert "hello".upper() == "HELLO"
assert len([1, 2, 3]) == 3

# Проверка с сообщением
age = 20
assert age >= 18, "Пользователь должен быть совершеннолетним"

# 10. ПРИМЕРЫ ДЛЯ QA
# ============================================

# Проверка длины строки
def check_title_length(title, max_length=100):
    """Проверка, что заголовок не длиннее max_length"""
    assert len(title) <= max_length, f"Заголовок слишком длинный: {len(title)}"
    return True

# Проверка email
def validate_email(email):
    """Проверка корректности email"""
    assert "@" in email, "Email должен содержать @"
    assert "." in email, "Email должен содержать точку"
    return True

# Проверка цены
def check_price(price):
    """Проверка, что цена положительная"""
    assert price > 0, "Цена должна быть положительной"
    assert isinstance(price, (int, float)), "Цена должна быть числом"
    return True

# 11. РАБОТА С JSON (для API тестов)
# ============================================

import json

# Создание JSON
data = {
    "name": "Ivan",
    "age": 19,
    "is_student": True
}

json_string = json.dumps(data)
print(json_string)

# Парсинг JSON
json_data = '{"name": "Maria", "age": 20}'
parsed = json.loads(json_data)
print(parsed["name"])  # Maria

# 12. КЛАССЫ (для Page Object)
# ============================================

class LoginPage:
    """Страница логина (пример Page Object)"""
    
    def __init__(self, driver):
        self.driver = driver
        self.username_field = "username"
        self.password_field = "password"
        self.login_button = "login"
    
    def enter_username(self, username):
        """Ввод логина"""
        print(f"Ввод логина: {username}")
        # driver.find_element(...).send_keys(username)
    
    def enter_password(self, password):
        """Ввод пароля"""
        print(f"Ввод пароля: {password}")
        # driver.find_element(...).send_keys(password)
    
    def click_login(self):
        """Нажатие кнопки входа"""
        print("Нажатие кнопки входа")
        # driver.find_element(...).click()
    
    def login(self, username, password):
        """Полный процесс входа"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# Использование
# login_page = LoginPage(driver)
# login_page.login("testuser", "password123")
