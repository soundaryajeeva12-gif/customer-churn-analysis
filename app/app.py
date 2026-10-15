import streamlit as st
import pandas as pd

st.title("Customer Churn Analysis Dashboard")
st.write("Exploring why customers leave and what drives churn risk")

from pathlib import Path
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(DATA_PATH)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])

st.write("### Raw Data Preview")
st.dataframe(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

st.write("## Churn Rate by Contract Type")

contract_churn = df.groupby('Contract')['Churn'].apply(
    lambda x: (x == 'Yes').mean() * 100
).reset_index()
contract_churn.columns = ['Contract', 'Churn Rate (%)']

fig1, ax1 = plt.subplots()
sns.barplot(data=contract_churn, x='Contract', y='Churn Rate (%)', ax=ax1)
ax1.set_title('Churn Rate by Contract Type')
st.pyplot(fig1)

st.write("## Churn Rate by Tenure Group")

df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,48,72], 
                              labels=['0-12','13-24','25-48','49+'])
tenure_churn = df.groupby('tenure_group', observed=True)['Churn'].apply(
    lambda x: (x == 'Yes').mean() * 100
).reset_index()
tenure_churn.columns = ['Tenure Group', 'Churn Rate (%)']

fig2, ax2 = plt.subplots()
sns.barplot(data=tenure_churn, x='Tenure Group', y='Churn Rate (%)', ax=ax2)
ax2.set_title('Churn Rate by Tenure Group')
st.pyplot(fig2)
st.write("## Try It: Check Churn Risk")

col1, col2 = st.columns(2)

with col1:
    selected_contract = st.selectbox("Contract Type", df['Contract'].unique())

with col2:
    selected_tenure_group = st.selectbox("Tenure Group", df['tenure_group'].cat.categories)

filtered = df[(df['Contract'] == selected_contract) & (df['tenure_group'] == selected_tenure_group)]

if len(filtered) > 0:
    risk = (filtered['Churn'] == 'Yes').mean() * 100
    st.metric("Churn Rate for this segment", f"{risk:.1f}%")
    st.write(f"Based on {len(filtered)} customers in this segment")
else:
    st.write("No customers found in this segment")
st.write("## Churn Playbook: Recommended Actions")
st.markdown("""
- **New month-to-month customers (0-12 months):** High-risk segment (51.4% churn) — offer a discounted contract upgrade early
- **Customers without tech support:** Churn at 41.65% vs 15.20% with support — offer a free trial in month 2-3
- **Fiber optic customers:** Month-to-month fiber customers churn at 54.6%, the riskiest segment — flag for service/satisfaction check-ins
- **Electronic check payers:** Churn at 45.3% vs 15-19% for other payment methods — incentivize switching to autopay""")