## Translator App
import streamlit as st
from googletrans import Translator
import pyttsx3

# translator and tts engine
translator = Translator()
engine = pyttsx3.init()

st.set_page_config(page_title="Translator", page_icon="🌍")

st.title("🌍 Language Translator App ")
st.write("Write something and translate it into another language.")

# input text
text = st.text_area("Enter your text:")

# languages
languages = ["en", "ur", "fr", "de", "es", "ar", "hi", "zh-cn"]

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("From", languages, index=0)
with col2:
    target = st.selectbox("To", languages, index=1)

# translate button
if st.button("Translate"):
    if text:
        result = translator.translate(text, src=source, dest=target)
        st.success("Done!")
        st.write("**Translated Text:**")
        st.write(result.text)

        # speak option
        if st.button("Speak"):
            engine.say(result.text)
            engine.runAndWait()
    else:
        st.warning("Please type something first.")
