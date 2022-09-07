
from crypt import methods
from flask import Flask, make_response, jsonify, request
from hidroDados import hidrometros
app = Flask(__name__)

@app.route('/hidrometros', methods={'GET'})
def getHidro():
    return make_response(
        jsonify(hidrometros)
    )    
app.run()

@app.route('/hidrometros', methods['POST']) #criando um novo hidrometro
def createHidro():
    hidro = request.json
    hidrometros.append(hidro)
    return hidro