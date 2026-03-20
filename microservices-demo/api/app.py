from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

AUTH_SERVICE_URL = "http://auth:5001/validate"


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    try:
        resposta = requests.post(AUTH_SERVICE_URL, json=dados, timeout=2)
        return jsonify({
            "api_status": "ok",
            "auth_response": resposta.json()
        }), resposta.status_code

    except requests.exceptions.Timeout:
        return jsonify({
            "api_status": "error",
            "message": "Timeout ao contactar o servico de autenticacao"
        }), 504

    except requests.exceptions.RequestException as e:
        return jsonify({
            "api_status": "error",
            "message": f"Erro ao contactar auth service: {str(e)}"
        }), 500


@app.route("/")
def home():
    return jsonify({"message": "API esta a correr"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
