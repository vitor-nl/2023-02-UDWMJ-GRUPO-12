class Product:
    def __init__(self, id: int, name: str, description: str, date_fabrication: str, 
    is_active: bool, category_id: int, unitary_price: float) -> None:
    
        self.id = id
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category_id = category_id
        self.unitary_price = unitary_price

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