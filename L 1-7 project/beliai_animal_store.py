from store import display_products, add_to_cart, remove_from_cart, checkout

def main():
    while True:
        print("\nДобро пожаловать в онлайн-магазин товаров для животных.")
        print("1. Посмотреть товары")
        print("2. Добавить товар в корзину")
        print("3. Удалить товар из корзины")
        print("4. оформить заказ")
        print("5. Выход")

        choise = input("Выберите действие (1-5): ")

        if choise == "1":
            display_products()
            
        elif choise == "2":
            product = input("Введите названия товара для добавления: ")
            add_to_cart(product)
            
        elif choise == "3":
            product = input("Введите названия товара для удаления: ")
            remove_from_cart(product)
            
        elif choise == "4":
            checkout()

        elif choise == "5":
            print("Спасибо, что воспользовались услугами нашего магазина!")
            break

        else:
            print("Ошибка! Попробуйте ввести снова одну цифру от 1 до 5.")

if __name__ == "__main__":
    main()