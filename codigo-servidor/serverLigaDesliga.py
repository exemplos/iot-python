from flask import Flask, abort, request, session
import json

app = Flask(__name__)

class Contexto:
    ligado = False


@app.route('/temphumid/send', methods=['POST']) 
def send():
    print(request.json)
    return "Ok... Python!"

@app.route('/temphumid/verifica') 
def verifica():
    if Contexto.ligado:
        return "on"
    else:
        return "off"

@app.route('/temphumid/on') 
def on():
    Contexto.ligado = True
    return "ligado"

@app.route('/temphumid/off') 
def off():
    Contexto.ligado = False
    return "desligado"

app.run(host='0.0.0.0', port=8080, debug=True)