from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets(name, emergency_contact) VALUES ( %s, %s ) RETURNING id"
    values = [vet.name, vet.emergency_contact]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['emergency_contact'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = Vet(result['name'], result['emergency_contact'], result['id'])
    return vet

def update(vet):
    sql = "UPDATE vets SET (name, emergency_contact) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.emergency_contact, vet.id]
    run_sql(sql, values)

