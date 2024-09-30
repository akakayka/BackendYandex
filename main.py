import requests
import json

base_url = "https://fakestoreapi.com/"

def print_value(value):
    for key, value in value.items():
        print("{0}: {1}".format(key, value))

print("Продукты, цена которых <20")
res = requests.get(f"{base_url}/products")
dict = res.json()
for product in dict:
    price = int(product["price"])
    if int(product["price"]) < 20:
        print_value(product)
        print()

print("Вывести все категории")
res = requests.get(f"{base_url}/products/categories").json()
print("\n".join(res))

print("\nВывести все продукты с категорией  \"jewelery\"")
res = requests.get(f"{base_url}/products/category/jewelery").json()
for product in res:
    print_value(product)
    print()

print("Вывести всех пользователей")
res = requests.get(f"{base_url}/users").json()
for user in res:
    print_value(user)
    print()


print("Добавить пользователя со своим именем")
new_user = {
                "email":'irst@mail.ru',
                "username":'akakaka',
                "password":'12345',
                "name":{
                    "firstname":'Timofey',
                    "lastname":'Tetushev'
                },
                "address":{
                    "city":'kilcoole',
                    "street":'7835 new road',
                    "number":3,
                    "zipcode":'12926-3874',
                    "geolocation":{
                        "lat":'-37.3159',
                        "long":'81.1496'
                    }
                },
            }
res = requests.post(f"{base_url}/users", json=new_user)
print("Статус ответа: "+res.status_code)