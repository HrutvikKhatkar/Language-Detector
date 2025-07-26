
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('language_model.pkl')

# Streamlit app
st.title("Devanagari Language Detection")

st.write("Enter a text in Hindi, Marathi, Sanskrit, or Nepali to detect its language.")

# Text input from the user
user_input = st.text_area("Enter text here:")

if st.button("Detect Language"):
    if user_input:
        # Predict the language
        prediction = model.predict([user_input])
        st.write(f"**Predicted Language:** {prediction[0]}")
    else:
        st.write("Please enter some text to detect the language.")
