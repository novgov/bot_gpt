# Словарь с товарами в магазине
magical_items = {
    "волшебная палочка": 100,
    "зелье здоровья": 50,
    "кристалл силы": 200,
    "амулет защиты": 150,
    "книга заклинаний": 300
}

def assort():
    for goods, price in magical_items.items():
        print(f"{goods}: {price} золотых монет")

def add_goods():
    item_name = input("Введите название нового товара: ")
    price = int(input(f"Введите цену для '{item_name}': "))
    magical_items[item_name] = price
    print(f"Товар '{item_name}' добавлен в ассортимент.")
    assort()

while True:
    action = input("Что вы хотите сделать? ").lower()
    if action == "добавить товар":
        add_goods()

    elif action == "изменить цену":
        item_name = input("Введите название товара, для которого хотите изменить цену: ")

        if item_name in magical_items:
            new_price = int(input(f"Введите новую цену для '{item_name}': "))

            print(f"Цена для '{item_name}' обновлена.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    elif action == "удалить товар":
        item_name = input("Введите название товара, который хотите удалить: ")

        if item_name in magical_items:
            del magical_items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    elif action == "посмотреть ассортимент":
        print("\nВаш текущий ассортимент:")
        for item, price in magical_items.items():
            print(f"{item}: {price} золотых монет")

    elif action == "закончить":
        break

    else:
        print("Неизвестная команда. Попробуйте еще раз.")

print("\nСпасибо за игру! Ваш финальный ассортимент:")
for item, price in magical_items.items():
    print(f"{item}: {price} золотых монет")