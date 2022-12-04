class Owner:
    def __init__(self, name, dob, phone, address, vet_id, owner_id=None):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.address = address
        self.vet_id = vet_id
        self.id = owner_id