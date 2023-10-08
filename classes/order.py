import uuid

class Order:

    def __init__(self, client_id, product, total_price):
        self.id = uuid.uuid4()
        self.client_id = client_id
        self.product = product
        self.total_price = total_price

    def export(self) -> dict:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product": self.product,
            "total_price": self.total_price
        }
    