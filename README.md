import streamlit as st

st.title("AI Mood Detector 😊")

user_input = st.text_input("Apna mood likho:")

def detect_mood(text):
    text = text.lower()
    if "happy" in text or "good" in text or "awesome" in text:
        return "😊 Happy"
    elif "sad" in text or "depressed" in text or "cry" in text:
        return "😢 Sad"
    elif "angry" in text or "mad" in text:
        return "😡 Angry"
    else:
        return "😐 Neutral"

if user_input:
    mood = detect_mood(user_input)
    st.write("Tumhara mood hai:", mood)
