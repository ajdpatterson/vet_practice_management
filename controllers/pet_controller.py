from flask import Flask, render_template, request, redirect, Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)