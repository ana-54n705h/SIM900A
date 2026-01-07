from flask import Flask, request
import base64

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    img = base64.b64decode(data["image"])

    with open("received.jpg", "wb") as f:
        f.write(img)

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
