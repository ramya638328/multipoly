import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

st.title("Weather Prediction App")

# --- Sample dataset ---
data = pd.DataFrame({
    'time_of_day': ['morning', 'afternoon', 'evening', 'night', 'morning', 'afternoon'],
    'temperature': [15, 25, 20, 10, 18, 30],
    'weather': ['sunny', 'sunny', 'cloudy', 'rainy', 'cloudy', 'sunny']
})

# Encode categorical variables
time_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

data['time_encoded'] = time_encoder.fit_transform(data['time_of_day'])
data['weather_encoded'] = weather_encoder.fit_transform(data['weather'])

# Train the model
X = data[['time_encoded', 'temperature']]
y = data['weather_encoded']
model = LogisticRegression()
model.fit(X, y)

# --- User input ---
time_input = st.selectbox("Select time of day", data['time_of_day'].unique())
temperature_input = st.number_input("Enter temperature (°C)", value=20, step=1)

# --- Prediction ---
if st.button("Predict Weather"):
    # Encode time
    time_num = time_encoder.transform([time_input])[0]
    
    # Predict weather
    prediction_encoded = model.predict([[time_num, temperature_input]])[0]
    prediction_label = weather_encoder.inverse_transform([prediction_encoded])[0]
    
    # Temperature-based season condition
    if temperature_input >= 28:
        season = "Hot 🌞"
    elif temperature_input >= 18:
        season = "Normal 🌤️"
    else:
        season = "Cold ❄️"
    
    # Final output
    st.success(
        f"⏰ Time of Day: {time_input.capitalize()}\n"
        f"🌡️ Temperature: {temperature_input} °C\n"
        f"🌦️ Predicted Weather: {prediction_label.capitalize()}\n"
        f"🔥 Condition: {season}"
    )
