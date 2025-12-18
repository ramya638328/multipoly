import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("/mnt/data/multipoly.pkl", "rb") as f:
    model = pickle.load(f)

# Mapping for Time of Day to numeric values
time_mapping = {
    "Morning": 0,
    "Afternoon": 1,
    "Evening": 2,
    "Night": 3
}

st.title("Weather Prediction App")

# User inputs
time_of_day_input = st.text_input("Enter Time of Day (Morning, Afternoon, Evening, Night):")
temperature_input = st.text_input("Enter Temperature:")

# Check if both inputs are provided
if st.button("Predict Weather"):
    if time_of_day_input not in time_mapping:
        st.error("Invalid Time of Day! Use Morning, Afternoon, Evening, or Night.")
    else:
        try:
            temperature_value = float(temperature_input)  # convert temperature to numeric
            # Prepare input dataframe for model
            input_df = pd.DataFrame([[time_mapping[time_of_day_input], temperature_value]],
                                    columns=["TimeOfDay", "Temperature"])
            
            # Make prediction
            prediction = model.predict(input_df)
            
            st.success(f"The predicted weather is: {prediction[0]}")
        except ValueError:
            st.error("Temperature must be a numeric value!")
            import streamlit as st
import pickle

uploaded_file = st.file_uploader("Upload your pickle model", type="pkl")

if uploaded_file is not None:
    model = pickle.load(uploaded_file)
    st.write("Model loaded successfully!")

