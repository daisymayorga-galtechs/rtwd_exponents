# streamlit_app.py
import streamlit as st

st.title("Exponents Explained: Math Magic for Repeating Multiplication!")
st.markdown("Think of exponents like a superhero shortcut in math. Instead of writing: 2 × 2 × 2 we just write: 2³. The small number (the 3) tells you how many times to multiply the big number (the 2) by itself. So, 2³ = 2 × 2 × 2 = 8 It’s like saying, “Hey 2, multiply yourself three times in a row!” ")


base = st.number_input("Enter a base:", value=2)
expo = st.number_input("Enter an exponent:", value=3)
result = base ** expo
st.write(f"{base} raised to the power of {expo} is {result}")
