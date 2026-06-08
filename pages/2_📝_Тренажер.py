from ai_helper import explain
from tasks import generate_task
from database import save_result
import inspect

import streamlit as st
if "role" not in st.session_state:
    st.switch_page("app.py")

if st.session_state["role"] != "student":
    st.warning("🛑 Страница доступна только ученикам.")
    st.stop()

st.title("📝 Тренажёр")

# Статистика
if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Показывать ли объяснение
if "show_help" not in st.session_state:
    st.session_state.show_help = False

# Создание первой задачи
if "question" not in st.session_state:
    question, answer = generate_task()
    st.session_state.question = question
    st.session_state.correct = answer

st.write(f"### {st.session_state.question}")

user_answer = st.number_input(
    "Введите ответ",
    value=0.0,
    step=1.0,
    key="answer_input"
)

# Проверка ответа
if st.button("Проверить"):

    st.session_state.attempts += 1

    if abs(user_answer - st.session_state.correct) < 0.001:

        st.session_state.score += 1
        st.session_state.show_help = False

        st.success("✅ Правильно!")

        save_result(
            st.session_state["user"],
            st.session_state.score,
            st.session_state.attempts
        )

    else:

        st.error("❌ Неверно!")
        st.session_state.show_help = True

# Кнопка объяснения
if st.session_state.show_help:

    if st.button("🤖 Объяснить решение", key="help_button"):

        st.info(
            explain(
                st.session_state.question
            )
        )

# Статистика
st.divider()

st.subheader("📊 Ваша статистика")

st.write(
    f"Правильных ответов: **{st.session_state.score}**"
)

st.write(
    f"Всего попыток: **{st.session_state.attempts}**"
)

if st.session_state.attempts > 0:

    percent = round(
        st.session_state.score /
        st.session_state.attempts * 100,
        1
    )

    st.progress(percent / 100)

    st.write(
        f"Успешность: **{percent}%**"
    )

# Новое задание
if st.button("Новое задание"):

    question, answer = generate_task()

    st.session_state.question = question
    st.session_state.correct = answer
    st.session_state.show_help = False

    st.rerun()
    