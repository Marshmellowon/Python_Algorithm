from dataclasses import dataclass

# 구조체
@dataclass
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 10

print(apple.price)
