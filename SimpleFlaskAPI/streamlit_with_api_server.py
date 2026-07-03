from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/page", methods=["POST"])
def generate_output():
    data = request.get_json()
    input1 = data["input1"]
    output = "Computer says _" + input1
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(port=5000)