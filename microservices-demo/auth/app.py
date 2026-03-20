from flask import Flask, request, jsonify
import time

app = Flask(__name__)


@app.route("/validate", methods=["POST"])
def validate():
    dados = request.get_json()

    username = dados.get("username")
    password = dados.get("password")

    if username == "raquel" and password == "1234":
        return jsonify({
            "auth_status": "success",
            "message": "Login valido"
        }), 200
    else:
        return jsonify({
            "auth_status": "fail",
            "message": "Credenciais invalidas"
        }), 401


@app.route("/")
def home():
    return jsonify({"message": "Auth service esta a correr"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
