import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("multipoly.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit app title
st.title("Weather Prediction App 🌤️")

st.write("Enter the details below to predict the weather:")

# Input fields
time_of_day = st.number_input("Time of Day (24-hour format, e.g., 14 for 2 PM):", min_value=0, max_value=23, value=12)
temperature = st.number_input("Temperature (°C):", value=25.0)

# Prediction button
if st.button("Predict Weather"):
    # Prepare input for the model
    input_data = np.array([[time_of_day, temperature]])
    
    # Predict
    prediction = model.predict(input_data)
    
    # Display the output
    st.success(f"The predicted weather is: {prediction[0]}")
