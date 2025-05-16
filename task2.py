import json
import tkinter as tk
from tkinter import messagebox, simpledialog


# Зчитування даних з JSON-файлу
with open('phones.json', 'r', encoding='utf-8') as file:
   phones = json.load(file)  # Завантаження списку телефонів


# Функція для оновлення списку телефонів на екрані
def refresh_list(data=None):
   listbox.delete(0, tk.END)  # Очищення списку
   for phone in data if data else phones:
       listbox.insert(tk.END, phone['name'])  # Додавання назв телефонів


# Функція для сортування телефонів
def sort_phones(criteria):
   sorted_list = sorted(phones, key=lambda x: x[criteria], reverse=True)
   refresh_list(sorted_list)


# Функція для пошуку телефону
def search_phone():
   query = simpledialog.askstring("Пошук", "Введіть назву або частину назви:")
   if query:
       results = [p for p in phones if query.lower() in p['name'].lower()]
       if results:
           refresh_list(results)
       else:
           messagebox.showinfo("Результат", "Нічого не знайдено.")


# Функція для показу деталей телефону
def show_details(event):
   selected = listbox.curselection()
   if selected:
       phone = phones[selected[0]]
       info = f"Назва: {phone['name']}\nЦіна: {phone['price']} USD\nРейтинг: {phone['rating']}\nВідгуки: {phone['reviews']}"
       messagebox.showinfo("Інформація про телефон", info)


# Створення головного вікна
root = tk.Tk()
root.title("Каталог телефонів")


# Кнопки
tk.Button(root, text="Сортувати за ціною", command=lambda: sort_phones('price')).pack()
tk.Button(root, text="Сортувати за рейтингом", command=lambda: sort_phones('rating')).pack()
tk.Button(root, text="Сортувати за відгуками", command=lambda: sort_phones('reviews')).pack()
tk.Button(root, text="Пошук", command=search_phone).pack()


# Список телефонів
listbox = tk.Listbox(root, width=50)
listbox.pack()
listbox.bind('<<ListboxSelect>>', show_details)


# Показати телефони при запуску
refresh_list()


root.mainloop()


