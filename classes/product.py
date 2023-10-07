class Product:
    def __init__(self, id: int, name: str, description: str) -> None:
        self.id = id
        self.name = name
        self.description = description

    def export(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }