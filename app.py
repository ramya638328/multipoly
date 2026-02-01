import streamlit as st

# Page config
st.set_page_config(
    page_title="Weather Prediction App",
    page_icon="🌦️",
    layout="centered"
)

# Function to change background image
def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Default background
set_bg("https://images.unsplash.com/photo-1501973801540-537f08ccae7b")  # neutral sky

# Title
st.title("🌦️ Weather Prediction App")
st.caption("Visual weather prediction with smart UI")

st.markdown("---")

# Input Section
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

predict = st.button("🔍 Predict Weather")

st.markdown("---")

# Prediction Section
if predict:

    # Simple logic (can be replaced by ML model)
    if temperature < 10:
        weather = "Cold"
        emoji = "❄️"
        condition = "Low Temperature"
        set_bg("https://images.unsplash.com/photo-1482192596544-9eb780fc7f66")
    elif temperature <= 30:
        weather = "Sunny"
        emoji = "☀️"
        condition = "Normal"
        set_bg("https://images.unsplash.com/photo-1502082553048-f009c37129b9")
    else:
        weather = "Hot"
        emoji = "🔥"
        condition = "High Temperature"
        set_bg("https://images.unsplash.com/photo-1504384308090-c894fdcc538d")

    # Result Card
    st.markdown(
        f"""
        <div style="
            background-color: rgba(255,255,255,0.85);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        ">
            <h3>📊 Prediction Result</h3>
            <p><b>⏰ Time of Day:</b> {time_of_day}</p>
            <p><b>🌡️ Temperature:</b> {temperature} °C</p>
            <p><b>{emoji} Weather:</b> {weather}</p>
            <p><b>🔥 Condition:</b> {condition}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


