
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Prosty perceptron
class Perceptron:
    def __init__(self, input_size, lr=1, epochs=10):
        self.W = np.zeros(input_size+1)
        self.lr = lr
        self.epochs = epochs

    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * x

# Tworzymy instancję perceptronu
input_size = 2  # Przykładowa liczba wejść
perceptron = Perceptron(input_size)

@app.route('/train', methods=['POST'])
def train():
    data = request.get_json()
    X = np.array(data['X'])
    y = np.array(data['y'])
    perceptron.fit(X, y)
    return jsonify({"message": "Model trained successfully"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = np.array(data['X'])
    prediction = perceptron.predict(X)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
