import requests
import json

BASE_URL = 'https://fakestoreapi.com'

# 1. Вывести все продукты дешевле 20
response = requests.get(f"{BASE_URL}/products")

products = response.json()

products_cheaper_20 = []

for product in products:
    if product['price'] < 20:
        products_cheaper_20.append(product)

print('Все продукты дешевле 20:', products_cheaper_20, sep='\n', end='\n\n')

# 2. Вывести все категории
response = requests.get(f"{BASE_URL}/products/categories")

categories = response.json()

print('Все категории:', categories, sep='\n', end='\n\n')

# 3. Вывести все продукты с категорией  "jewelery"
response = requests.get(f"{BASE_URL}/products/category/jewelery")

jewelery_products = response.json()

print('Все продукты с категорией "jewelery":', jewelery_products, sep='\n', end='\n\n')

# 4. Вывести всех пользователей
response = requests.get(f"{BASE_URL}/users")

users = response.json()

print('Все пользователи:', users, sep='\n', end='\n\n')

# 5. Добавить пользователя со своим именем

new_user = {
    "email": "example@example.com",
    "username": "exampleuser",
    "password": "password123",
    "name": {
        "firstname": "Example",
        "lastname": "User"
    },
    "address": {
        "city": "New York",
        "street": "123 Main St",
        "number": "123",
        "zipcode": "12345",
        "geolocation": {
            "lat": "40.7128",
            "long": "74.0060"
        }
    },
    "phone": "123-456-7890"
}

response = requests.post(f"{BASE_URL}/users", data=json.dumps(new_user), headers={'Content-Type': 'application/json'})

if response.status_code == 200 or response.status_code == 201:
    print("Пользователь добавлен:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)

# Насколько понял, в ответе должны вернуться параметры созданного пользователя,
# но в данном случае возвращается только id, при этом status_code - 200, перепробовал разные варианты