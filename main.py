import streamlit as st
import openai
import os
from config import LANGUAGES, LANGUAGE_STRINGS, TONES
from utils import LegalPromptGenerator
from dotenv import load_dotenv
load_dotenv()

LANGUAGE_ICONS = {
    "English": "🇺🇸",
    "中文": "🇨🇳",
    "हिन्दी": "🇮🇳",
    "Español": "🇪🇸",
    "Français": "🇫🇷",
    "Deutsch": "🇩🇪",
    "العربية": "🇸🇦",
}

st.set_page_config(page_title="AI Legal Advisor", page_icon="⚖️", layout="wide")

def main():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_language = st.radio(
            LANGUAGE_STRINGS['en']['language_label'], 
            list(LANGUAGE_ICONS.keys()),
            format_func=lambda x: f"{LANGUAGE_ICONS[x]} {x}",
            horizontal=True
        )

    with col2:
        selected_tone = st.selectbox(
            "Consultation Tone", 
            list(TONES.keys())
        )

    language_code = LANGUAGES[selected_language]
    strings = LANGUAGE_STRINGS[language_code]

    print(f"Selected Language: {selected_language} ({language_code})")

    st.title(strings['title'])
    st.markdown(strings['description'])

    st.sidebar.title("About Legally")
    st.sidebar.info(strings['disclaimer'])

    country = st.text_input(strings['country_label'])
    role = st.text_input(strings['role_label'])
    situation = st.text_area(strings['situation_label'])
    need_agreement = st.checkbox(strings['agreement_label'])

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.markdown(f"**{message['role']}**: {message['content']}")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    if st.button(strings['get_analysis_btn']):
        if not openai.api_key:
            st.error("API Key not set.")
            return
        if not situation or not country:
            st.error("Please provide a situation and country.")
            return

        try:

            prompt = LegalPromptGenerator.generate_prompt(
                situation, 
                country, 
                role,
                TONES[selected_tone],  
                language_code, 
                need_agreement
            )


            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are a highly skilled and experienced legal advisor with expertise in international law. Your advice should be clear, practical, and tailored to the user's specific legal situation. {TONES[selected_tone]}"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500
            )

            st.session_state.messages.append({"role": "user", "content": situation})
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response['choices'][0]['message']['content']
            })

            st.subheader(strings['analysis_title'])
            st.write(response['choices'][0]['message']['content'])

        except Exception as e:
            st.error(f"Error processing request: {str(e)}")

if __name__ == "__main__":
    main()