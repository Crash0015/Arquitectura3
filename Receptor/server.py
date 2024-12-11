from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/webhook", methods=["POST"])
def webhook_listener():
    """
    Escucha solicitudes del WebHook
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
              event:
                type: string
    responses:
      200:
        description: Datos recibidos exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                data:
                  type: object
    """
    data = request.json
    print(f"Datos recibidos: {data}")
    return jsonify({"status": "received", "data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
