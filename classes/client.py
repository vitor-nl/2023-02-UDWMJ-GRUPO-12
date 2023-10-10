import uuid

class Client:

    def __init__(self, object):
        self.id = uuid.uuid4()
        self.first_name = object["first_name"]
        self.last_name = object["last_name"]
        self.address = object["address"]
        self.phone = object["phone"]
        self.email = object["email"]
        self.social_network_id = object["social_network_id"]

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
    