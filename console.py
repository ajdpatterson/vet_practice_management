import pdb

from models.vet import Vet
from models.owner import Owner
from models.pet import Pet

import repositories.owner_respository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet_repository.delete_all()
owner_repository.delete_all()
pet_repository.delete_all()

vet1 = Vet("Alan Rickman", "Wife - 07772123123")
vet_repository.save(vet1)
vet2 = Vet("Jane Jones", "Daughter - 07777123123")
vet_repository.save(vet2)
vet3 = Vet("Bill Bones", "Friend - 01419871232")
vet_repository.save(vet3)

owner1 = Owner("Linda Hamilton", "1985-03-01", "07773444664", "12 Station Road", vet1.id)
owner_repository.save(owner1)
owner2 = Owner("Terry Jeffries", "1977-04-12", "07777444333", "4 Main Street", vet1.id)
owner_repository.save(owner2)
owner3 = Owner("Jim Jobs", "1982-10-19", "07777838383", "18 Golf Road", vet2.id)
owner_repository.save(owner3)
owner4 = Owner("William Gates", "1995-06-04", "07888999777", "14c Shell Street", vet2.id)
owner_repository.save(owner4)
owner5 = Owner("Sally Slaps", "1966-12-12", "07888444333", "54 Clarance Drive", vet3.id)
owner_repository.save(owner5)
owner6 = Owner("Petra Pistol", "1987-01-23", "07666555444", "657 Main Street", vet3.id)
owner_repository.save(owner6)
owner7 = Owner("Jill McJill", "1981-02-03", "07444222111", "12 Divis Drive", vet3.id)
owner_repository.save(owner7)

pet1 = Pet("Mittens", "2020-02-01", "cat", owner1.id, owner1.vet_id, notes=None)
pet_repository.save(pet1)
pet2 = Pet("Dobby", "2019-05-05", "dog", owner1.id, owner1.vet_id, notes=None)
pet_repository.save(pet2)
pet3 = Pet("Swift", "2018-04-06", "horse", owner2.id, owner2.vet_id, notes=None)
pet_repository.save(pet3)
pet4 = Pet("Chip", "2020-02-20", "dog", owner3.id, owner3.vet_id, notes=None)
pet_repository.save(pet4)
pet5 = Pet("Smudge", "2017-05-24", "cat", owner4.id, owner4.vet_id, notes=None)
pet_repository.save(pet5)
pet6 = Pet("Casper", "2016-06-01", "dog", owner5.id, owner5.vet_id, notes=None)
pet_repository.save(pet6)
pet7 = Pet("Lil Sebastian", "2015-05-01", "horse", owner5.id, owner5.vet_id, notes=None)
pet_repository.save(pet7)
pet8 = Pet("Gecko", "2014-04-04", "dog", owner6.id, owner6.vet_id, notes=None)
pet_repository.save(pet8)
pet9 = Pet("Buttons", "2017-07-09", "cat", owner7.id, owner7.vet_id, notes=None)
pet_repository.save(pet9)
pet10 = Pet("Peachy", "2014-01-21", "cat", owner7.id, owner7.vet_id, notes=None)
pet_repository.save(pet10)