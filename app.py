import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Analysis", layout="wide")
df=pd.read_csv("European_Bank.csv")

st.title("Customer Churn Analysis Dashboard")
c1,c2,c3=st.columns(3)
c1.metric("Total Customers", len(df))
if "Exited" in df.columns:
    c2.metric("Churn Rate", f"{df['Exited'].mean()*100:.2f}%")
if "Geography" in df.columns:
    c3.metric("Countries", df["Geography"].nunique())

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Columns")
st.write(['Year', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited'])
