# pip install flask
# conda install flask

from flask import Flask, abort, request 
import json

app = Flask(__name__)


@app.route('/temphumid/send', methods=['POST']) 
def send():
    print(request.json)
    return "Ok... Python!"

@app.route('/ok123', methods=['GET']) 
def retorna():
    return "Ok...!"

app.run(host='0.0.0.0', port=8080, debug=True)

