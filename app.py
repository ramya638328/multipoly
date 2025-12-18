import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

st.title("Weather Prediction App - Polynomial Regression")

# 1️⃣ Hardcoded dataset
data = {
    "Time_of_Day": ["Morning", "Afternoon", "Evening", "Night", "Morning", "Afternoon", "Evening", "Night"],
    "Temperature": [20, 30, 25, 15, 22, 32, 27, 18],
    "Weather": ["Sunny", "Sunny", "Cloudy", "Rainy", "Sunny", "Sunny", "Cloudy", "Rainy"]
}
df = pd.DataFrame(data)
st.subheader("Dataset")
st.dataframe(df)

# 2️⃣ Encode categorical data
time_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

df["Time_Code"] = time_encoder.fit_transform(df["Time_of_Day"])
df["Weather_Code"] = weather_encoder.fit_transform(df["Weather"])

# 3️⃣ Features and target
X = df[["Time_Code", "Temperature"]]
y = df["Weather_Code"]

# 4️⃣ Train polynomial regression model (degree 2)
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X, y)

# 5️⃣ Predict weather for dataset
df["Predicted_Code"] = model.predict(X).round().astype(int)
df["Predicted_Weather"] = weather_encoder.inverse_transform(df["Predicted_Code"])

# 6️⃣ Display predictions
st.subheader("Predicted Weather")
st.dataframe(df[["Time_of_Day", "Temperature", "Predicted_Weather"]])
