import pandas as pd
from urllib.parse import urlparse
import string

# -------------------------------------------------------------------
# feature_extractor.py
# -------------------------------------------------------------------
# This script extracts basic features from a predefined list of URLs.
# These features are saved as features.csv to be used for model training.
#
# NOTE: Later and in a production setting, we will replace these sample URLs with real data.
# -------------------------------------------------------------------

# Sample phishing-like URLs (for demonstration purposes only)
phishing_urls = [
    "http://free-iphone16-verification-now-login.com/win/offer.html",
    "http://facebook.com-login.verify-suspicious.net",
    "https://google.com.wxts.net/login.php"
]

# Sample legitimate URLs
legit_urls = [
    "https://facebook.com",
    "https://apple.com",
    "https://huawei.com"
]

# Construct combined dataset
all_urls = phishing_urls + legit_urls
labels = [1]*len(phishing_urls) + [0]*len(legit_urls)  # 1 = phishing, 0 = legitimate

def extract_features(url):
    """Extracts a set of simple features from a given URL."""
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
    
    # Count special characters often abundant in phishing URLs
    special_chars = set(string.punctuation)
    special_count = sum(ch in special_chars for ch in url)

    return {
        "url": url,
        "url_length": url_length,
        "domain_length": domain_length,
        "path_length": path_length,
        "subdomain_count": subdomain_count,
        "https_flag": https_flag,
        "special_char_count": special_count
    }

# Extract features for all URLs
features = [extract_features(u) for u in all_urls]
df = pd.DataFrame(features)
df['label'] = labels

# Save the extracted features
df.to_csv("features.csv", index=False)
print("Feature extraction complete! Data saved to features.csv")