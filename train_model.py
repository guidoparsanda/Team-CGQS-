import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# -------------------------------------------------------------------
# train_model.py
# -------------------------------------------------------------------
# This script trains a Random Forest model on the extracted features.
# It saves the model to model.pkl.
#
# NOTE: This is a prototype. Accuracy on this subtle, synthetic dataset
# is not representative of real-world performance.
# -------------------------------------------------------------------

# Load extracted features
data = pd.read_csv("features.csv")

# Select relevant columns (exclude URL string itself)
X = data[["url_length", "domain_length", "path_length", "subdomain_count", "https_flag", "special_char_count"]]
y = data["label"]

# Initialize and train a simple Random Forest model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Save the trained model
dump(model, "model.pkl")
print("Model trained and saved as model.pkl")

# Optional: Quick accuracy check (not meaningful with tiny fake dataset)
accuracy = model.score(X, y)
print(f"Training Accuracy (synthetic data): {accuracy*100:.2f}%")