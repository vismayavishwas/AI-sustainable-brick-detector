import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv", comment="#")

# Features
X = data[['peak', 'energy', 'decay_time']]

# Labels
y = data['label']

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X, y)

# Save model
joblib.dump(model, "brick_model.pkl")

print("Model trained and saved!")
