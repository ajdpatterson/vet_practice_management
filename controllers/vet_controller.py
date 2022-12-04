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
    return render_template('/vets/vet.html', vet=vet)

@vets_blueprint.route("/vets/new_vet")
def new_vet():
    return render_template('/vets/new_vet.html')