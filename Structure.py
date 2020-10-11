from dataclasses import dataclass


# 구조체
@dataclass
class Product:
    weight: int = None
    price: float = None

    def area(self):
        return self.weight * self.price


apple = Product()
apple.price = 10

print(apple.price)
