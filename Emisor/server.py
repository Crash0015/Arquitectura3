from flask import Flask, jsonify
from flasgger import Swagger
import requests

app = Flask(__name__)
swagger = Swagger(app)

# URL del WebHook receptor
WEBHOOK_URL = "http://receptor:5001/webhook"

@app.route("/")
def home():
    """
    Página de inicio del Emisor
    ---
    responses:
      200:
        description: Página inicial
        content:
          text/html:
            schema:
              type: string
    """
    return """
    <h1>Bienvenido al Emisor de WebHooks</h1>
    <p>Prueba los endpoints:</p>
    <ul>
        <li><a href="/trigger">Enviar un WebHook</a></li>
        <li><a href="/apidocs">Documentación Swagger</a></li>
    </ul>
    """

@app.route("/trigger", methods=["GET"])
def trigger_webhook():
    """
    Dispara un evento simulando un WebHook
    ---
    responses:
      200:
        description: El WebHook se envió exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                response:
                  type: string
      500:
        description: Error al enviar el WebHook
    """
    payload = {"message": "¡Hola desde el WebHook emisor!", "event": "Hola Mundo"}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
