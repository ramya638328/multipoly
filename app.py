import streamlit as st

st.set_page_config(page_title="Weather Prediction", layout="centered")

st.title("🌦️ Smart Weather Prediction")

# Input Card
with st.container():
    st.subheader("🧾 Input Parameters")
    time_of_day = st.selectbox(
        "⏰ Time of Day",
        ["Morning", "Afternoon", "Evening", "Night"]
    )
    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=0,
        max_value=50
    )

predict = st.button("🔮 Predict Weather")

if predict:
    # Simple logic
    if temperature >= 30:
        weather = "Hot"
        color = "error"
    elif temperature >= 20:
        weather = "Sunny"
        color = "success"
    else:
        weather = "Cold"
        color = "info"

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if color == "success":
        st.success(f"☀️ Weather: {weather}")
    elif color == "error":
        st.error(f"🔥 Weather: {weather}")
    else:
        st.info(f"❄️ Weather: {weather}")

    st.markdown(
        f"""
        **⏰ Time of Day:** {time_of_day}  
        **🌡️ Temperature:** {temperature} °C  
        """
    )

    st.caption(
        "ℹ️ Prediction is based on temperature range and time of day."
    )
