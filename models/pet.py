class Pet:
    def __init__(self, name, dob, type, owner_id, vet_id, notes, pet_id=None):
        self.name = name
        self.dob = dob
        self.type = type
        self.owner_id = owner_id
        self.vet_id = vet_id
        self.notes = notes
        self.id = pet_id
