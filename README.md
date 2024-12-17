# PhishLens ML Model Showcase Prototype
---

## Project Overview

For this current version of **PhishLens**, we will showcase our prototype that we designed for a hackathon demonstration, showcasing how a simple ML model can help detect phishing URLs (for now we kept it simple). We hope that this prototype highlights feasibility, explainability, and potential pathways for future enhancement.

With **PhishLens**, we:

- Demonstrate how key URL features can be extracted for ML-based phishing detection.
- Emphasize transparency using explainability tools (e.g., SHAP).
- Present a vision for integration with a browser extension UI (inspired by provided Figma designs), allowing for real-time user alerts and enhanced cybersecurity posture.

**Note:** This is an early-stage prototype. Real-world efficacy would require richer datasets and feature engineering.

---

## Key Features

1. **Feature Extraction from URLs**:  
   - URL length  
   - Domain length  
   - Path length  
   - Subdomain count  
   - Presence of HTTPS  
   - Special character count

2. **Lightweight ML Model (Random Forest)**:  
   Trains quickly and is easy to interpret—perfect for a hackathon demonstration.

3. **Explainability via SHAP**:  
   Provides insights into which features most influence predictions, fostering trust and understanding.

---

## Why This Matters

Phishing attacks leverage deceptive links to trick users into revealing credentials or sensitive data. **PhishLens** aims to show how an ML-driven approach can detect suspicious URLs before users fall victim, enhancing security measures and reducing organizational risk.

---

## Technology Stack

- **Language**: Python 3.x
- **Libraries**:  
  - `pandas` for data handling  
  - `scikit-learn` for machine learning  
  - `shap` for explainability  
  - `joblib` for model persistence

---

## Repository Structure

- `feature_extractor.py`: Extracts basic features from a sample of URLs and saves them to `features.csv`.
- `train_model.py`: Trains a Random Forest model on the extracted features and saves the model as `model.pkl`.
- `predict_prototype.py`: Loads the trained model, predicts on new URLs, and demonstrates SHAP-based explainability.

**Note:** `features.csv` is generated after running `feature_extractor.py`.

---

Figma UI (that we submitted in a separate link, for your convenience, here's the link https://www.figma.com/design/dPkoMKyaIMncIHONrRvJC6/PhishLens?node-id=0-1&t=aSXrmJv3I1wzox6r-1)

We envision a browser extension interface (as hinted in our Figma design):

- Users visiting suspicious links see immediate alerts from PhishLens.
- A user-friendly dashboard displays intercepted suspicious URLs, risk levels, and top contributing factors.
- Our ML backbone (this prototype) can be integrated into such a UI, showcasing how raw ML transforms into a practical security tool.

---

## Explainability with SHAP

Explainability is crucial. SHAP values highlight which features contributed most to a particular prediction. This level of transparency:

- Helps security teams trust and refine the model.
- Educates stakeholders on how ML-driven decisions are made.
- Ensures the system isn’t a "black box," vital in cybersecurity scenarios.

---

## Future Improvements

- **Data Expansion**: Integrate real phishing data from sources like PhishTank.
- **Feature Engineering**: Incorporate domain age, WHOIS info, lexical patterns, and more.
- **Model Tuning**: Experiment with advanced models (XGBoost, LightGBM) and hyperparameter optimization.
- **Deployment**: Package into a microservice or connect directly to a backend for browser extensions.

---

## Our Current Use Case: Browser Extension

**PhishLens** is designed to integrate into a browser extension scenario:

- **Real-Time Scanning**: Every visited URL is checked against the ML model instantly.
- **User Alerts**: Warns users before they interact with suspicious pages.
- **Enterprise Defense**: Deployed organization-wide to enhance corporate cybersecurity posture.

---

## Hackathon Planning

- **Time Constraints**: We focused on a functional prototype rather than a perfect solution.
- **Simplicity**: The code is accessible, easily reviewed, and quick to run.
- **Early Submission**: Ready ahead of time to avoid last-minute issues.

---

## Acknowledgments

- **Hackathon Organizers & Mentors**: Thanks for your guidance, feedback, and inspiration.
- **Teammates & Collaborators**: Rapid ideation, coding, and iteration made this possible.
- **Community & Tools**:
  - PhishTank for real-world phishing references.
  - Scikit-learn and SHAP for ML and explainability resources.

---
