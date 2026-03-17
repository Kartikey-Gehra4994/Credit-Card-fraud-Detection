# Credit Card Fraud Detection

This project builds a machine learning model to detect fraudulent credit card transactions.
The system analyzes transaction features and predicts whether a transaction is **Fraudulent** or **Normal**.

The project also includes a **Flask web application** where users can paste transaction feature values and get an instant prediction.

---

## Live App
Checkout Link : 
```
https://credit-card-fraud-detection-lv.onrender.com
```

## Ex Features
Normal :
```
0.7645459184216227,-0.9639741597402978,0.1719562613420123,-0.9027194662010714,0.09886236844877479,0.40305921181292165,0.5142053466590302,-0.22925891641182633,0.016835570555720596,0.8086235692441269,-2.121099002869872,0.6722475591734016,1.614935455985687,0.5969685328837052,-0.06617707657780006,-0.15144205784950934,0.3635779407377648,1.1174761914220974,-0.2494256362588582,0.07870650039141351,-0.2433868303307131,-0.923255497294336,-0.47764118176261194,-1.5012128739736477,0.825755058476264,2.226301777448765,-0.3732720030904187,-0.0043011192230137775,22766.69
```
Fraud : 
```
-0.3678622414867012,0.525590661905547,-0.5007998435159446,0.31880842783065055,-0.35032713927735065,-1.2277794572919314,-0.4106984382558888,0.2054426940982071,0.008947541400544,-0.9332237554111467,1.084411022741452,-1.1988914577769512,0.4222290139347142,-0.890202479577038,0.08639733675418641,-0.6423944698254003,-0.5007225392804132,-0.3127640050589851,-0.3285319438552679,0.20262808908171162,0.09214086821500357,-0.5425561595788102,0.010347580477831176,0.802885660059549,-0.007163691482137588,0.6774212005519649,0.3977117422219321,0.4701699272309738,1360.6
```


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
