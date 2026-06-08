import streamlit as st
from ai_helper import ask_ai
if "role" not in st.session_state:
    st.switch_page("app.py")
st.title("🤖 ИИ-помощник")

question = st.text_area(
    "Введите вопрос по теме «Проценты»"
)

if st.button("Получить ответ"):

    if question.strip() == "":
        st.warning("Введите вопрос.")
    else:

        with st.spinner("ИИ думает..."):

            answer = ask_ai(question)

        st.success(answer)
        