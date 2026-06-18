import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load data
data = pd.read_csv("dataset.csv", comment="#")

# Load model
model = joblib.load("brick_model.pkl")

# Feature importance
importance = model.feature_importances_

features = [
    "Peak",
    "Energy",
    "Decay Time",
    "Stability"
]

# GRAPH 1
plt.figure(figsize=(7,5))
plt.bar(features, importance)
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.savefig("feature_importance.png")
plt.close()

# GRAPH 2
plt.figure(figsize=(6,6))
data['label'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.title("Class Distribution")
plt.ylabel("")
plt.savefig("class_distribution.png")
plt.close()

# GRAPH 3
plt.figure(figsize=(7,5))

for label in data['label'].unique():
    subset = data[data['label'] == label]

    plt.scatter(
        subset['peak'],
        subset['energy'],
        label=label
    )

plt.xlabel("Peak")
plt.ylabel("Energy")
plt.title("Peak vs Energy")
plt.legend()

plt.savefig("peak_vs_energy.png")
plt.close()

print("Graphs saved")
