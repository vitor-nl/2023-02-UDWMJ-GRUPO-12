import uuid

class Person:

    def __init__(self, first_name, last_name, address, phone, email, social_network_id=None):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.social_network_id = social_network_id

    def export(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "social_network_id": self.social_network_id
        }
    