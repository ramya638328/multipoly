import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_excel("day.xlsx")

# Encoders
le_time = LabelEncoder()
le_temp = LabelEncoder()
le_weather = LabelEncoder()

df['Time_of_Day'] = le_time.fit_transform(df['Time_of_Day'])
df['Temperature_Level'] = le_temp.fit_transform(df['Temperature_Level'])
df['Weather'] = le_weather.fit_transform(df['Weather'])

X = df[['Time_of_Day', 'Temperature_Level']]
y = df['Weather']

# Polynomial Features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Train model
model = LogisticRegression(
    multi_class='multinomial',
    solver='lbfgs',
    max_iter=1000
)
model.fit(X_poly, y)

# Streamlit UI
st.title("🌦️ Weather Prediction App")

time_input = st.selectbox(
    "Select Time of Day",
    le_time.classes_
)

temp_input = st.selectbox(
    "Select Temperature Level",
    le_temp.classes_
)

if st.button("Predict Weather"):
    input_data = [[
        le_time.transform([time_input])[0],
        le_temp.transform([temp_input])[0]
    ]]
    
    input_poly = poly.transform(input_data)
    prediction = model.predict(input_poly)
    
    weather = le_weather.inverse_transform(prediction)
    
    st.success(f"Predicted Weather: {weather[0]}")
