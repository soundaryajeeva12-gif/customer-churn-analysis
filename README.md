# Customer Churn Analysis

## Problem Statement
A telecom company wants to understand which customers are likely to churn 
and why, so it can take targeted action to retain them before they leave.

## Dataset
[Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) 
(IBM sample dataset via Kaggle) — 7,043 customer records with demographic, 
account, and service information.

## Approach
1. **Data Cleaning:** Fixed `TotalCharges` (stored as text due to blank values 
   for 11 new customers), dropped rows with missing values (<0.2% of data).
2. **SQL Analysis:** Queried churn rate across tenure groups, contract types, 
   and tech support status using SQLite.
3. **EDA & Visualization:** Built charts to confirm patterns found in SQL.
4. **Modeling:** Built a Logistic Regression model to predict churn.
5. **Dashboard:** Built an interactive Streamlit dashboard for live exploration.

## Key Findings
- **Tenure:** New customers (0-12 months) churn at **47.7%**, vs just **9.5%** 
  for customers with 49+ months tenure — a ~5x difference.
- **Contract type:** Month-to-month customers churn at **42.7%**, vs **11.3%** 
  for one-year and **2.9%** for two-year contracts — a ~15x difference.
- **Tech support:** Customers without tech support churn at **41.7%**, vs 
  **15.2%** for those with it — nearly 3x higher.

## Model Performance
- Accuracy: 79% — but accuracy is misleading here due to class imbalance 
  (~26.5% churn rate).
- Recall on churners: 52% — the model misses about half of actual churners.
- **Given the business cost of missing a churner vs. a false alarm, I'd 
  prioritize recall over precision in a production version** — e.g. via 
  class weighting or threshold tuning.

## Churn Playbook (Recommended Actions)
1. New month-to-month customers → offer discounted contract upgrade early
2. Customers without tech support → offer free trial in month 2-3
3. Fiber optic customers → flag for service/satisfaction check-ins
4. Electronic check payers → incentivize switch to autopay

## Tech Stack
Python, Pandas, NumPy, SQLite, Matplotlib, Seaborn, Scikit-learn, Streamlit

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What I'd Improve With More Time
- Address class imbalance (SMOTE or class weighting) to improve recall
- Compare against Random Forest / XGBoost
- Segment playbook recommendations by customer value, not just churn risk