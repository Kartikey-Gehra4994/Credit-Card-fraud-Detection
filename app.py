from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# load model
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        input_data = request.form['features']

        # split values
        values = [float(x) for x in input_data.split(',')]

        # check feature count
        if len(values) != 29:
            return render_template(
                "index.html",
                prediction_text="Please enter exactly 29 values separated by commas."
            )

        data = np.array([values])

        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Fraud Transaction"
        else:
            result = "Normal Transaction"

        return render_template("index.html", prediction_text=result)

    except ValueError:
        return render_template(
            "index.html",
            prediction_text="Invalid input. Please enter numeric values separated by commas."
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error occurred: {str(e)}"
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)