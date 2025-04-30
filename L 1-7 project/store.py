#  Доступные товары и их цены
products = {
    "Корм для собак": 10,
    "Корм для котов": 8,
    "Игрушка для собак": 15,
    "Игрушка для котов": 20,
    "Клетка для птиц": 75,
    "Лежак для животного": 100
}

#  Корзина пользователя
cart = []

def display_products():
    """выводит список доступных товаров и их цен."""
    print("Доступные товары:")
    for product, price in products.items():
        print(f"{product}: {price} бел руб.")

def add_to_cart(product):
    """Добавляет товар в корзину, если он доступен."""
    if product in products:
        cart.append(product)
        print(f"{product} добавлен в корзину.")
    else:
        print("Товар не найден.")

def remove_from_cart(product):
    """Удаляет товар из корзины."""
    if product in cart:
        cart.remove(product)
        print(f"{product} удален из корзины.")
    else:
        print("Товар не найден в корзине.")

def checkout():
    """Оформляет заказ и выводит итоговую сумму."""
    if not cart:
        print("Корзина пуста")
        return

    total = sum(products[product] for product in cart)
    print("Ваш заказ:")
    for product in cart:
        print(f" - {product}: {products[product]} бел руб.")
    print(f"Итого: {total} бел руб.")