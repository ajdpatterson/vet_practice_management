from flask import Flask, render_template, request, redirect, Blueprint
from models.owner import Owner
import repositories.owner_respository as owner_repository

owners_blueprint = Blueprint("owners", __name__)