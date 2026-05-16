import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="KetanWeather", page_icon="🌤️", layout="centered")

st.title("🌤️ KetsWeather")
st.caption("AI-powered weather assistant")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("API Key", type="password", value="sk-...")
    base_url = st.text_input("Base URL", value="https://api.openai.com/v1")
    model = st.text_input("Model", value="gpt-4o-mini")

city = st.text_input("Enter city name", placeholder="e.g. Mumbai, New York, London")

if st.button("Get Weather", type="primary", disabled=not city.strip()):
    if not api_key or api_key == "sk-...":
        st.error("Please enter your API key in the sidebar.")
    else:
        with st.spinner(f"Fetching weather for {city}..."):
            try:
                client = OpenAI(api_key=api_key, base_url=base_url)
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a weather assistant. Provide current weather conditions "
                                "for the requested city. Include temperature (Celsius and Fahrenheit), "
                                "conditions, humidity, wind speed, and a brief forecast. "
                                "Format your response clearly with emojis for readability. "
                                "If you don't have real-time data, provide typical seasonal weather "
                                "for that location and note it's an estimate."
                            ),
                        },
                        {
                            "role": "user",
                            "content": f"What's the current weather in {city}?",
                        },
                    ],
                    temperature=0.7,
                    max_tokens=500,
                )
                weather_info = response.choices[0].message.content
                st.success(f"Weather for **{city}**")
                st.markdown(weather_info)
            except Exception as e:
                st.error(f"Error: {e}")
