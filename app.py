from flask import Flask, render_template

from controllers.vet_controller import vets_blueprint
from controllers.owner_controller import owners_blueprint
from controllers.pet_controller import pets_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(pets_blueprint)

@app.route('/')
def home():
    return render_template('/vets/index.html')