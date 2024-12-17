import shap
from joblib import load
from urllib.parse import urlparse
import string

# -------------------------------------------------------------------
# predict_prototype.py
# -------------------------------------------------------------------
# This script loads the saved model (model.pkl) and uses it to predict
# on a new set of URLs. It also demonstrates the use of SHAP values
# to explain the model's predictions.
#
# For demonstration, we use a few sample URLs. Replace or prompt user
# input as desired.
# -------------------------------------------------------------------

# Load the previously trained model
model = load("model.pkl")

def extract_single_url_features(url):
    """Extracts features from a single URL for prediction."""
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path
    scheme = parsed.scheme

    url_length = len(url)
    domain_length = len(domain)
    path_length = len(path)
    subdomains = domain.split('.')
    subdomain_count = len(subdomains) - 2 if len(subdomains) > 2 else 0
    https_flag = 1 if scheme == "https" else 0

    special_chars = set(string.punctuation)
    special_count = sum(ch in special_chars for ch in url)

    return [url_length, domain_length, path_length, subdomain_count, https_flag, special_count]

# Test URLs
test_urls = [
    "http://free-iphone16-verification-now-login.com/win/offer.html",  # Likely phishing
    "https://facebook.com",  # Likely legitimate
    "https://apple.com/login"  # Likely legitimate
]

# Prepare features for prediction
X_test = [extract_single_url_features(url) for url in test_urls]

# Predict using the loaded model
preds = model.predict(X_test)

# Display predictions
for url, pred in zip(test_urls, preds):
    label = "Phishing" if pred == 1 else "Legitimate"
    print(f"URL: {url}\nPrediction: {label}\n")

# Explainability with SHAP
# TreeExplainer works well for tree-based models like RandomForest
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

print("SHAP explainability ready. If running locally, uncomment the summary plot code below to visualize.")

# Uncomment the line below to visualize SHAP summary if running locally:
# shap.summary_plot(shap_values[1], X_test, feature_names=["url_length","domain_length","path_length","subdomain_count","https_flag","special_char_count"])