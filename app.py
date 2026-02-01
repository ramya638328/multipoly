import streamlit as st

st.set_page_config(
    page_title="Weather Prediction App",
    page_icon="🌦️",
    layout="centered"
)

st.title("🌦️ Weather Prediction App")
st.caption("Visual output based on prediction")

st.markdown("---")

# Inputs
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

predict = st.button("🔍 Predict")

st.markdown("---")

if predict:

    # Weather logic
    if temperature < 10:
        weather = "Rainy"
        emoji = "🌧️"
        image_path = "images/rainy.jpg"
    elif temperature <= 30:
        weather = "Sunny"
        emoji = "☀️"
        image_path = "images/sunny.jpg"
    else:
        weather = "Hot"
        emoji = "🔥"
        image_path = "images/hot.jpg"

    # Result card
    st.markdown(
        f"""
        <div style="
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        ">
            <h3>📊 Prediction Result</h3>
            <p><b>⏰ Time of Day:</b> {time_of_day}</p>
            <p><b>🌡️ Temperature:</b> {temperature} °C</p>
            <p><b>{emoji} Weather:</b> {weather}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🌄 Visual Representation")
    st.image(
        image_path,
        caption=f"{weather} condition representation",
        use_container_width=True
    )

    st.info(
        "The displayed image visually represents the predicted weather condition."
    )

st.markdown("---")
st.caption("🚀 Image-based output for better user experience")
