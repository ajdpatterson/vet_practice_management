from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

def save(pet):
    sql = "INSERT INTO pets(name, dob, type, owner_id, vet_id, notes) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [pet.name, pet.dob, pet.type, pet.owner_id, pet.vet_id, pet.notes]
    results = run_sql( sql, values )
    # breakpoint()
    pet.id = results[0]['id']
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        pet = Pet(result['name'], result['dob'], result['type'], result['owner_id'], result['vet_id'], result['notes'], result['id'])
    return pet