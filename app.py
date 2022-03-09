from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict():

    sepal_length = request.json.get("sepal_length")
    sepal_width = request.json.get("sepal_width")
    petal_length = request.json.get("petal_length")
    petal_width = request.json.get("petal_width")

    dic = validate(sepal_length, sepal_width, petal_length, petal_width)

    if dic:
        return jsonify(dic), 400

    classification = get_classification(sepal_length, sepal_width, petal_length, petal_width)

    # return jsonify({"sepal_length":sepal_length, "sepal_width":sepal_width, "petal_length": petal_length, "petal_width":petal_width, "class":classification})
    return jsonify({"class":classification})

def validate(sl, sw, pl, pw) -> list:
    # input validation
    ret = []

    if not sl: ret.append("Variável sepal_length não informada")
    if not sw: ret.append("Variável sepal_width não informada")
    if not pl: ret.append("Variável petal_length não informada")
    if not pw: ret.append("Variável petal_width não informada")

    return ret

def get_classification(sl, sw, pl, pw):
    return "Iris-versicolor"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)