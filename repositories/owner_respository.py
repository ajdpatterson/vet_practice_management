from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners(name, dob, phone, address, vet_id) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [owner.name, owner.dob, owner.phone, owner.address, owner.vet_id]
    results = run_sql( sql, values )
    owner.id = results[0]['id']
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = Owner(result['name'], result['dob'], result['phone'], result['address'], result['vet_id'], result['id'])
    return owner