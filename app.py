import streamlit as st
from deep_translator import GoogleTranslator
from translator import LANGUAGES

st.title("🌍 Language Translator")
st.caption("Translate text between multiple languages instantly.")

# Name input
name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name}! 👋")

# Language selection
source = st.selectbox("Source Language", list(LANGUAGES.keys()))
target = st.selectbox("Target Language", list(LANGUAGES.keys()))

# Text input
text = st.text_area("Enter text", placeholder="Type something to translate...")

# Buttons
col1, col2 = st.columns(2)
translate_btn = col1.button("🔄 Translate")

if translate_btn:
    if not name.strip():
        st.warning("Please enter your name.")
    elif not text.strip():
        st.warning("⚠️ Please enter text to translate.")
    elif source == target:
        st.warning("⚠️ Source and target languages cannot be the same.")
    else:
        try:
            with st.spinner("Translating..."):
                translated = GoogleTranslator(
                    source=LANGUAGES[source], target=LANGUAGES[target]
                ).translate(text)

            st.success("Translation completed successfully!")
            st.subheader("✅ Translation Result")
            with st.container():
                st.markdown(f"**👤 User:** {name}")
                st.markdown(f"**🌐 Source Language:** {source}")
                st.markdown(f"**🎯 Target Language:** {target}")

                st.write("**Original Text**")
                st.write(text)

                st.write("**Translated Text**")
                st.divider()
                st.text_area(
                    "Translated Text", translated, height=100, key="translated"
                )

        except Exception:
            st.error(
                "Translation failed. Please check your internet connection or selected language."
            )

st.divider()

st.caption("Developed by Maira Khan • CodeAlpha AI Internship 2026")
