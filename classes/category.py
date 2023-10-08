class Category:
    def __init__(self, object) -> None:
        self.id = object["id"]
        self.name = object["name"]
        self.description = object["description"]

    def export(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }