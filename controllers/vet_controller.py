from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/")
def vets():
    vets = vet_repository.select_all()
    return render_template("/vets/index.html", vets=vets)

@vets_blueprint.route("/vets/<id>/display")
def display_vet(id):
    vet = vet_repository.select(id)
    registered_owners = vet_repository.show_registered_owners(id)
    return render_template('/vets/vet.html', vet=vet, registered_owners=registered_owners)

@vets_blueprint.route("/vets/new_vet/")
def new_vet():
    return render_template('/vets/new_vet.html')

@vets_blueprint.route("/vets/new_vet/", methods=["POST"])
def create_vet():
    name = request.form['name']
    emergency_contact = request.form["emergency_contact"]
    new_vet = Vet(name, emergency_contact)
    vet_repository.save(new_vet)
    return redirect("/")

@vets_blueprint.route('/vets/<id>/delete/', methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/")

@vets_blueprint.route('/vets/<id>/edit/')
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('/vets/edit.html' ,vet=vet)

@vets_blueprint.route('/vets/<id>/', methods=["POST"])
def update_vet(id):
    name = request.form["name"]
    emergency_contact = request.form['emergency_contact']
    vet = Vet(name, emergency_contact, id)
    vet_repository.update(vet)
    return redirect("/")
