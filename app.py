import streamlit as st
import pickle
import pandas as pd

st.title("Weather Prediction App - Polynomial Regression")

# Load trained model and encoders
with open("weather_model.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
time_encoder = data["time_encoder"]
weather_encoder = data["weather_encoder"]

# Hardcoded dataset for display
df = pd.DataFrame({
    "Time_of_Day": ["Morning", "Afternoon", "Evening", "Night"],
    "Temperature": [20, 30, 25, 15]
})

st.subheader("Dataset")
st.dataframe(df)

# Encode input for prediction
df["Time_Code"] = time_encoder.transform(df["Time_of_Day"])
X = df[["Time_Code", "Temperature"]]

# Predict weather
df["Predicted_Code"] = model.predict(X).round().astype(int)
df["Predicted_Weather"] = weather_encoder.inverse_transform(df["Predicted_Code"])

st.subheader("Predicted Weather")
st.dataframe(df[["Time_of_Day", "Temperature", "Predicted_Weather"]])
