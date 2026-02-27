from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# POST form handling
@app.route("/predict", methods=["POST"])
def predict():
    name = request.form["name"]
    marks = int(request.form["marks"])

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return f"{name} Result: {result}"

# JSON API endpoint
@app.route("/api/result/<int:marks>")
def api_result(marks):
    if marks >= 40:
        return jsonify({"result": "Pass"})
    else:
        return jsonify({"result": "Fail"})

if __name__ == "__main__":
    app.run(debug=True)