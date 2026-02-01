import streamlit as st

# Page config
st.set_page_config(
    page_title="Weather Prediction App",
    page_icon="🌦️",
    layout="centered"
)

# Title
st.title("🌦️ Weather Prediction App")
st.caption("An interactive weather prediction system")

st.markdown("---")

# 🔹 Input Section
st.subheader("🧾 Input Parameters")

time_of_day = st.selectbox(
    "⏰ Select Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

temperature = st.number_input(
    "🌡️ Enter Temperature (°C)",
    min_value=-10,
    max_value=50,
    value=20
)

# Predict button
predict = st.button("🔍 Predict Weather")

st.markdown("---")

# 🔹 Prediction Logic + UI
if predict:

    # Simple rule-based logic (replace with ML model later)
    if temperature < 10:
        weather = "Cold"
        emoji = "❄️"
        bg_color = "#D6EAF8"
        condition = "Low Temperature"
    elif temperature <= 30:
        weather = "Sunny"
        emoji = "☀️"
        bg_color = "#FCF3CF"
        condition = "Normal"
    else:
        weather = "Hot"
        emoji = "🔥"
        bg_color = "#FADBD8"
        condition = "High Temperature"

    # 🌈 Result Card
    st.markdown(
        f"""
        <div style="
            background-color:{bg_color};
            padding:20px;
            border-radius:12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        ">
            <h3>📊 Prediction Result</h3>
            <p><b>⏰ Time of Day:</b> {time_of_day}</p>
            <p><b>🌡️ Temperature:</b> {temperature} °C</p>
            <p><b>{emoji} Predicted Weather:</b> {weather}</p>
            <p><b>🔥 Condition:</b> {condition}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

   
