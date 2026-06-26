
import streamlit as st

st.title("AI Mood Detector 😊")

user_input = st.text_input("Apna mood likho:")

if user_input:
    text = user_input.lower()
    
    if "happy" in text:
        st.success("😊 You are Happy!")
    elif "sad" in text:
        st.error("😢 You are Sad!")
    elif "angry" in text:
        st.warning("😡 You are Angry!")
    else:
        st.info("😐 Mood samajh nahi aaya")
