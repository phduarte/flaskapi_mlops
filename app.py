from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/predict",methods=['POST'])
def predict():

    sepal_length = request.json.get("sepal_length")
    sepal_width = request.json.get("sepal_width")
    petal_length = request.json.get("petal_length")
    petal_width = request.json.get("petal_width")

    dic = validate(sepal_length, sepal_width, petal_length, petal_width)

    if dic:
        return jsonify(dic), 400

    arr = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    iris = model.predict(arr)[0]
    classification = get_classification(iris)

    return jsonify({"class":classification})

def validate(sl, sw, pl, pw) -> list:
    # input validation
    ret = []

    if not sl: ret.append("Variável sepal_length não informada")
    if not sw: ret.append("Variável sepal_width não informada")
    if not pl: ret.append("Variável petal_length não informada")
    if not pw: ret.append("Variável petal_width não informada")
    if not is_float(sl): ret.append("Variável sepal_length não é um valor válido.")
    if not is_float(sw): ret.append("Variável sepal_width não é um valor válido.")
    if not is_float(pl): ret.append("Variável petal_length não é um valor válido.")
    if not is_float(pw): ret.append("Variável petal_width não é um valor válido.")

    return ret

def get_classification(classification:int):
    return {0:"Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}[classification]

def is_float(val:str) -> bool:
    try:
        float(val)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)