from flask import Flask, request
import base64
import time
import os

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    img = base64.b64decode(data["image"])

    filename = f"image_{int(time.time())}.jpg"
    with open(filename, "wb") as f:
        f.write(img)

    return "OK", 200

@app.route("/")
def home():
    return "SIM900A Server Running", 200

if __name__ == "__main__":
    # Render provides PORT automatically
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
