import streamlit as st

def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Inputs
st.title("🌦️ Smart Weather Prediction")

time_of_day = st.selectbox("⏰ Select Time of Day", 
                            ["Morning", "Afternoon", "Evening", "Night"])
temperature = st.number_input("🌡️ Enter Temperature (°C)", min_value=0, max_value=50)

# Background selection
if time_of_day == "Morning":
    set_bg("https://images.unsplash.com/photo-1502082553048-f009c37129b9")
elif time_of_day == "Afternoon":
    set_bg("https://images.unsplash.com/photo-1501785888041-af3ef285b470")
elif time_of_day == "Evening":
    set_bg("https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d")
else:
    set_bg("https://images.unsplash.com/photo-1504384308090-c894fdcc538d")

# Predict button
if st.button("🔮 Predict"):
    weather = "Sunny" if temperature > 20 else "Cold"

    st.markdown("## 📊 Prediction Result")
    st.success(f"""
    ⏰ Time of Day: **{time_of_day}**  
    🌡️ Temperature: **{temperature} °C**  
    ☀️ Weather: **{weather}**
    """)

    st.info("ℹ️ The prediction is based on temperature and time of day.")
