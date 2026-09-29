from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], float(data["price"]), int(data["quantity"]))
