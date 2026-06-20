import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset.csv", comment="#")

# Load trained model
model = joblib.load("brick_model.pkl")

# Features
X = data[['peak', 'energy', 'decay_time']]
y = data['label']

# -------------------------
# 1. FEATURE IMPORTANCE
# -------------------------

importance = model.feature_importances_

features = [
    'Peak',
    'Energy',
    'Decay Time'
]

plt.figure(figsize=(7,5))
plt.bar(features, importance)
plt.title("Feature Importance in Random Forest")
plt.ylabel("Importance Score")
plt.show()

# -------------------------
# 2. CLASS DISTRIBUTION
# -------------------------

plt.figure(figsize=(6,6))
y.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Dataset Class Distribution")
plt.ylabel("")
plt.show()

# -------------------------
# 3. PEAK VS ENERGY
# -------------------------

labels = data['label'].unique()

plt.figure(figsize=(7,5))

for label in labels:
    subset = data[data['label'] == label]
    plt.scatter(
        subset['peak'],
        subset['energy'],
        label=label
    )

plt.xlabel("Peak")
plt.ylabel("Energy")
plt.title("Peak vs Energy Classification")
plt.legend()
plt.show()
