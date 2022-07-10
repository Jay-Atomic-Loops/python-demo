from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route("/api")
def api():
    return jsonify({"message":"Hello world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
