from datetime import date

# Базовий 
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def update_stock(self, amount):
        if amount < 0:
            raise ValueError("Кількість товару не може бути від’ємною.")
        return amount

    def display_info(self):
        print(f"[{self.product_id}] Назва: {self.name}, Ціна: {self.price} грн")


class FoodProduct(Product):
    def __init__(self, product_id, name, price, expiry_date):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date

    def display_info(self):
        super().display_info()
        print(f"   Термін придатності: {self.expiry_date}")


class ElectronicsProduct(Product):
    def __init__(self, product_id, name, price, warranty_period, brand):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"   Бренд: {self.brand}, Гарантія: {self.warranty_period} міс.")


#Склад
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products = []  

    def add_product(self, product, count):
        for i, (p, c) in enumerate(self.products):
            if p.product_id == product.product_id:
                self.products[i] = (p, c + count)
                return
        self.products.append((product, count))

    def remove_product(self, product_id, count):
        for i, (p, c) in enumerate(self.products):
            if p.product_id == product_id:
                if c < count:
                    raise ValueError("На складі недостатньо товару для видалення.")
                new_count = c - count
                if new_count == 0:
                    del self.products[i]
                else:
                    self.products[i] = (p, new_count)
                return
        raise ValueError("Товар не знайдено.")

    def find_product_by_id(self, product_id):
        for p, c in self.products:
            if p.product_id == product_id:
                return p, c
        return None

    def display_inventory(self):
        print(f"\nІнвентаризація складу: {self.name}")
        for product, count in self.products:
            product.display_info()
            print(f"   Кількість на складі: {count}")
            print("-" * 40)

# товари
apple = FoodProduct("FP001", "Яблуко", 12.5, date(2025, 1, 15))
laptop = ElectronicsProduct("EP001", "Ноутбук", 25000, 24, "HP")

# склад
warehouse = Warehouse("Центральний склад")

warehouse.add_product(apple, 100)
warehouse.add_product(laptop, 10)

warehouse.display_inventory()

# Пошук
product, qty = warehouse.find_product_by_id("FP001")
print(f"\nЗнайдено товар: {product.name}, Кількість: {qty}")

# видалення 
warehouse.remove_product("FP001", 20)
warehouse.display_inventory()
