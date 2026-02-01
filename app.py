import streamlit as st

# Page config
st.set_page_config(
    page_title="Weather Prediction",
    page_icon="🌦️",
    layout="centered"
)

# 🌈 Gradient Header
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg, #4facfe, #00f2fe);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f9f9f9;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}
.result {
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>🌦️ Weather Prediction App</h1>
    <p>Simple • Smart • User Friendly</p>
</div>
""", unsafe_allow_html=True)

# 🧾 Input Card
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧾 Enter Weather Details")

time_of_day = st.selectbox(
    "⏰ Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

temperature = st.number_input(
    "🌡️ Temperature (°C)",
    min_value=-10,
    max_value=50,
    value=20
)

predict = st.button("🔍 Predict")
st.markdown("</div>", unsafe_allow_html=True)

# 📊 Result Card
if predict:

    if temperature < 10:
        weather = "Cold"
        emoji = "❄️"
        note = "Low temperature detected"
    elif temperature <= 30:
        weather = "Sunny"
        emoji = "☀️"
        note = "Normal temperature range"
    else:
        weather = "Hot"
        emoji = "🔥"
        note = "High temperature detected"

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h3>📊 Prediction Result</h3>
        <p class="result">{emoji} {weather}</p>
        <p>⏰ <b>Time:</b> {time_of_day}</p>
        <p>🌡️ <b>Temperature:</b> {temperature} °C</p>
        <p>ℹ️ {note}</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Prediction completed successfully")

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.caption("🚀 Frontend enhanced for better user experience")
