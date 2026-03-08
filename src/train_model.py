import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# load dataset
df = pd.read_csv(r"C:\Users\MY LOQ\OneDrive\Desktop\credit-card-fraud-detection\data\creditcard_2023.csv")

# features and target
X = df.drop(['Class','id'], axis=1)
y = df['Class']

# split data
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print('Start Model training')

# model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(x_train_scaled, y_train)

# prediction
y_pred = rf_model.predict(x_test_scaled)

# accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# save model
joblib.dump(rf_model, r"C:\Users\MY LOQ\OneDrive\Desktop\credit-card-fraud-detection\models\random_forest_model.pkl")