from models import Product

products = []

while True:
    print("\n1. Добави продукт")
    print("2. Покажи продукти")
    print("3. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        name = input("Име: ")
        quantity = int(input("Количество: "))

        product = Product(name, quantity)
        products.append(product)

        print("Продуктът е добавен")

    elif choice == "2":
        if len(products) == 0:
            print("Няма продукти")
        else:
            for product in products:
                product.show_product()
                product.check_stock()

    elif choice == "3":
        print("Изход...")
        break

    else:
        print("Невалидна опция")