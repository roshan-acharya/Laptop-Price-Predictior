# 💻 Laptop Price Prediction

A Machine Learning-powered web app that predicts laptop prices based on specifications using data scraped from [Mudita Store](https://mudita.com.np). Built using XGBoost, Scikit-learn, and deployed on Streamlit Cloud.

---

## 🚀 Overview

This project aims to help users estimate the price of a laptop based on its specifications. It can be useful for buyers, sellers, and analysts looking to understand price trends in the Nepali tech market.

---

## 🕸️ Data Collection

- **Website Scraped**: [https://mudita.com.np](https://mudita.com.np)
- **Tool Used**: [Playwright](https://playwright.dev/python/) (for handling JavaScript-rendered content)
- **Total Records**: ~300 laptops
- **Collected Features**:
  - Brand
  - Series
  - Processor
  - RAM
  - Storage
  - Graphics Card
  - Price (Target)

---


### 📚 Libraries Used:
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `xgboost`
- `pickle`
- `streamlit`

### 🔁 Steps Followed:
1. **Data Scraping** using Playwright
2. **Data Cleaning & Preprocessing**
   - Removed outliers and missing values
   - Encoded categorical variables
3. **Feature Engineering**
   - Combined similar features
   - Extracted numerical values where needed
4. **Model Training**
   - Tried various ML models: Linear Regression, Random Forest, XGBoost
   - Final Model: `XGBoostRegressor`
   - Also tested an Ensemble (VotingRegressor) model
5. **Model Evaluation**
6. **Model Saving** using `pickle`
7. **Web App Interface** using `Streamlit`
8. **Deployment** on `Streamlit Cloud`

---

## 📈 Model Performance

| Metric              | Value                     |
|---------------------|---------------------------|
| Mean Squared Error  | 3,562,120,926.05          |
| R² Score            | 0.6107                    |

> The model explains approximately 61% of the variation in laptop prices.

---

## 🌐 Live Demo

👉 **[Click here to try the app on Streamlit Cloud](https://laptop-price-predictior-np.streamlit.app/)**  


---

## 🖥️ Local Setup

### 🔧 Prerequisites
- Python 3.8+
- pip

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/laptop-price-predictor-np.git
cd laptop-price-predictor-np

# Install required libraries
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```
👨‍💻 Author
Made with ❤️ by Roshan Acharya

Aspiring Machine Learning Developer from Nepal
