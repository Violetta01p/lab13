import json
import tkinter as tk
from tkinter import messagebox, simpledialog


# Зчитування даних з файлу phones.json
with open('phones.json', 'r', encoding='utf-8') as f:
   phones = json.load(f)  # Створено змінну phones — список телефонів


# Функція для оновлення списку телефонів
def refresh_list():
   listbox.delete(0, tk.END)  # Очистити список
   for phone in phones:
       listbox.insert(tk.END, phone['name'])  # Додати назви телефонів


# Функція для показу деталей вибраного телефону
def show_details(event):
   idx = listbox.curselection()  # Отримати індекс вибраного елемента
   if idx:
       phone = phones[idx[0]]  # Отримати відповідний телефон
       info = f"Назва: {phone['name']}\nЦіна: {phone['price']} USD\nРейтинг: {phone['rating']}\nВідгуки: {phone['reviews']}"
       messagebox.showinfo("Деталі телефону", info)  # Показати інформацію


# Функція для пошуку телефону за назвою
def search():
   query = simpledialog.askstring("Пошук", "Введіть назву або частину назви:")
   if query:
       results = [p for p in phones if query.lower() in p['name'].lower()]
       listbox.delete(0, tk.END)  # Очистити список
       for phone in results:
           listbox.insert(tk.END, phone['name'])  # Додати знайдені телефони


# Функція для сортування за ціною
def sort_by_price():
   global phones
   phones = sorted(phones, key=lambda x: x['price'])  # Сортування за ціною (від дешевших до дорожчих)
   refresh_list()  # Оновити список після сортування


# Створення головного вікна
root = tk.Tk()
root.title("Список телефонів")


# Кнопка сортування
btn_sort_price = tk.Button(root, text="Сортувати за ціною", command=sort_by_price)
btn_sort_price.pack()


# Кнопка пошуку
btn_search = tk.Button(root, text="Пошук телефону", command=search)
btn_search.pack()


# Список для відображення телефонів
listbox = tk.Listbox(root, width=50)
listbox.pack()
listbox.bind('<<ListboxSelect>>', show_details)  # Показати деталі при виборі телефону


# Початкове заповнення списку
refresh_list()


# Запуск вікна
root.mainloop()

