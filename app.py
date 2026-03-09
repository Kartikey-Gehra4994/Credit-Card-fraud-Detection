from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# model load
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    input_data = request.form['features']
    values = [float(x) for x in input_data.split(',')]
    data = np.array([values])
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Fraud Transaction"
    else:
        result = "Normal Transaction"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)