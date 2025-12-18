import streamlit as st
import pickle

st.title("Multipoly Model Prediction")

# Use relative path: make sure multipoly.pkl is in the same folder as app.py
try:
    with open("multipoly.pkl", "rb") as f:
        model = pickle.load(f)
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("Error: multipoly.pkl file not found. Make sure it is in the same folder as app.py.")

# Example input for prediction
time_of_day = st.number_input("Enter time of day (hour)", min_value=0, max_value=23)
temperature = st.number_input("Enter temperature (°C)")

if st.button("Predict Weather"):
    try:
        # Replace this with your actual model prediction code
        prediction = model.predict([[time_of_day, temperature]])
        st.write(f"Predicted Weather: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

