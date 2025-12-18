import streamlit as st
import pickle

st.title("Multipoly Model Prediction")

uploaded_file = st.file_uploader("Upload your trained model (.pkl)", type="pkl")

if uploaded_file is not None:
    model = pickle.load(uploaded_file)
    st.success("Model loaded successfully!")

    time_of_day = st.number_input("Enter time of day (hour)", min_value=0, max_value=23)
    temperature = st.number_input("Enter temperature (°C)")

    if st.button("Predict Weather"):
        try:
            prediction = model.predict([[time_of_day, temperature]])
            st.write(f"Predicted Weather: {prediction[0]}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
else:
    st.info("Please upload a trained model (.pkl file) to continue.")
