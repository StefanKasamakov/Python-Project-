class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def show_product(self):
        print(f"Продукт: {self.name}")
        print(f"Количество: {self.quantity}")

    def check_stock(self):
        if self.quantity > 0:
            print("Има наличност")
        else:
            print("Няма наличност")