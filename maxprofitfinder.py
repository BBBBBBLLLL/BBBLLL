import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Financial Planning Calculator")

st.title("Financial Planning Calculator")

st.header("**Monthly Income**")
st.subheader("Salary")
colAnnualSal, colTax = st.beta_columns(2)

with colAnnualSal:
    salary = st.number_input("Enter your annual salary($): ", min_value=0.0, format='%f')
with colTax:
    tax_rate = st.number_input("Enter your tax rate(%): ", min_value=0.0, format='%f')

tax_rate = tax_rate / 100.0
salary_after_taxes = salary * (1 - tax_rate)
monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)
view rawBudgetApp_part3.py hosted with ❤ by GitHub
