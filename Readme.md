# Credit Card Fraud Detection

This project builds a machine learning model to detect fraudulent credit card transactions.
The system analyzes transaction features and predicts whether a transaction is **Fraudulent** or **Normal**.

The project also includes a **Flask web application** where users can paste transaction feature values and get an instant prediction.

---

# Project Goal

The goal of this project is to apply **machine learning techniques** to identify suspicious credit card transactions and help reduce financial fraud.

---

# Project Structure

```
credit-card-fraud-detection
│
├── data
│   └── creditcard.csv
│
├── notebooks
│   └── fraud_analysis.ipynb
│
├── src
│   └── train_model.py
│
├── models
│   └── random_forest_model.pkl
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
├── app.py
├── requirements.txt
├── Procfile
└── README.md
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML / CSS
* Jupyter Notebook

---

# Machine Learning Workflow

1. Load the credit card transaction dataset
2. Perform data exploration and preprocessing
3. Select relevant features
4. Split dataset into training and testing sets
5. Train machine learning models
6. Evaluate model performance
7. Save the trained model using **Joblib**

---

# Model Performance

The Random Forest model achieved very high performance on the dataset.

Example result:

```
Accuracy: 0.9998
```

The model successfully identifies fraudulent transactions with high precision and recall.

---

# Web Application

A simple **Flask web app** is included in this project.

Users can:

* Paste all **29 transaction feature values**
* Click the **Predict** button
* Instantly see whether the transaction is **Fraud** or **Normal**

---

# How to Run the Project Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

### 2. Navigate to the project folder

```
cd credit-card-fraud-detection
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Flask application

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

# Model Input Format

The web app expects **29 feature values separated by commas**.

Example:

```
0.1,-1.2,0.5,0.3,...,120
```

These values represent transaction features used by the trained model.

---

# Future Improvements

Possible improvements for this project:

* Improve UI and user experience
* Add probability score for fraud prediction
* Deploy using Docker
* Add API endpoint for predictions
* Use deep learning models for comparison

---

# Author

Kartikey Gehra

---

# License

This project is open-source and available for learning and educational purposes.
