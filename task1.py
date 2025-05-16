import json


phones = [
   {"name": "iPhone 13", "price": 1200, "rating": 4.5, "reviews": 150},
   {"name": "Samsung Galaxy S21", "price": 900, "rating": 4.3, "reviews": 120},
   {"name": "Xiaomi Mi 11", "price": 700, "rating": 4.2, "reviews": 80}
]


with open('phones.json', 'w', encoding='utf-8') as f:
   json.dump(phones, f, ensure_ascii=False, indent=4)
