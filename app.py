import streamlit as st

st.set_page_config(
    page_title="Авторизация",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Авторизация")

role = st.radio(
    "Выберите роль",
    ["Ученик", "Учитель"]
)

if role == "Ученик":

    fio = st.text_input("Фамилия Имя")
    school_class = st.text_input("Класс")

    if st.button("Войти"):

        if fio != "" and school_class != "":

            st.session_state["role"] = "student"
            st.session_state["user"] = f"{fio} ({school_class})"

            st.switch_page("pages/0_🏠_Главная.py")

        else:

            st.warning("Заполните все поля.")

else:

    password = st.text_input(
        "Пароль",
        type="password"
    )

    if st.button("Войти"):

        if password == "teacher123":

            st.session_state["role"] = "teacher"

            st.switch_page("pages/0_🏠_Главная.py")

        else:

            st.error("Неверный пароль.")