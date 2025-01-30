# Using Flask and Scikit-Learn to deploy a simple machine learning model
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import pickle

app = Flask(__name__)

# Training a simple model
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = SVC()
model.fit(X_train, y_train)

# Saving the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    
    # Loading the model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
