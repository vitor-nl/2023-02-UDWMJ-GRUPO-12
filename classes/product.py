class Product:
    def __init__(self, object) -> None:
    
        self.id = object["id"]
        self.name = object["name"]
        self.description = object["description"]
        self.date_fabrication = object["date_fabrication"]
        self.is_active = object["is_active"]
        self.category_id = object["category_id"]
        self.unitary_price = object["unitary_price"]

    def export(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_fabrication": self.date_fabrication,
            "is_active": self.is_active,
            "category_id": self.category_id,
            "unitary_price": self.unitary_price,
        }