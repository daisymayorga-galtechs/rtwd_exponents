# streamlit_app.py
import streamlit as st

base = st.number_input("Enter a base:", value=2)
expo = st.number_input("Enter an exponent:", value=3)
result = base ** expo
st.write(f"{base} raised to the power of {expo} is {result}")
