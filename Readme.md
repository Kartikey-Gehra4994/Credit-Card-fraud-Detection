# Credit Card Fraud Detection

This project builds a machine learning model to detect fraudulent credit card transactions.
The model learns patterns from transaction data and predicts whether a transaction is **fraud** or **not fraud**.

## Project Goal

The goal of this project is to use machine learning to identify suspicious credit card transactions and help reduce financial fraud.

## Project Structure

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
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Jupyter Notebook
* Random Forest Classifier

## Steps in the Project

1. Load the credit card transaction dataset.
2. Perform basic data exploration.
3. Prepare the data for machine learning.
4. Split the data into training and testing sets.
5. Train a Random Forest model.
6. Evaluate the model using accuracy.
7. Save the trained model.

## Model Performance

The Random Forest model achieved very high accuracy on the dataset.

Example result:

```
Accuracy: 0.9998
```

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

2. Go to the project folder

```
cd credit-card-fraud-detection
```

3. Install required libraries

```
pip install -r requirements.txt
```

4. Run the training script

```
python src/train_model.py
```

## Output

After running the script, the trained model will be saved in the **models** folder as:

```
random_forest_model.pkl
```

## Future Improvements

* Handle class imbalance better
* Try other machine learning models
* Build a web app for real-time fraud detection
* Deploy the model

## Author

Kartikey Gehra
