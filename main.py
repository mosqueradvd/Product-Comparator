from flask import Flask, request, jsonify, render_template
from bardapi import Bard
import os

# Configuración de la clave de API para Bard
os.environ[
    '_BARD_API_KEY'] = "fQgr57Ch5PW-cdnK-aBugcYnWjgm37f4JXQrBiSEOrJyyGTCAxJzZMhJe1cXlGPb0vtpxQ."

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response", methods=["GET"])
def get_response():
    input_text = request.args.get("input_text")

    if input_text:
        question = f"Cuál es la tienda con el precio mas bajo para el: {input_text} en USA? y dime en qué link puedo ver esa informacion, no es necesario que me expliques nada más."
        respuesta = Bard().get_answer(question)['content']
    else:
        respuesta = ""

    return jsonify({"contenedor": respuesta})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
