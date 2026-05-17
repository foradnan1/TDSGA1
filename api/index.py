from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    data = request.json

    return jsonify({
        "message": "POST received",
        "data": data
    })
