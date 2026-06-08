import streamlit as st

if "role" not in st.session_state:
    st.switch_page("app.py")

st.title("📚 Интерактивное изучение темы «Проценты»")

if st.session_state["role"] == "student":
    st.success(f"👋 Добро пожаловать, {st.session_state['user']}!")
else:
    st.success("👨‍🏫 Добро пожаловать, преподаватель!")

st.write("### Выберите раздел приложения")

col1, col2 = st.columns(2)

with col1:
    if st.button("📖 Теория", use_container_width=True):
        st.switch_page("pages/1_📖_Теория.py")

    if st.button("📝 Тренажёр", use_container_width=True):
        st.switch_page("pages/2_📝_Тренажер.py")

with col2:
    if st.button("🤖 ИИ-помощник", use_container_width=True):
        st.switch_page("pages/3_🤖_ИИ_помощник.py")

    if st.button("📈 Мои результаты", use_container_width=True):
        st.switch_page("pages/4_📈_Мои_результаты.py")

# Кнопка статистики только для учителя
if st.session_state["role"] == "teacher":
    if st.button("📊 Статистика учеников", use_container_width=True):
        st.switch_page("pages/5_📈_Статистика.py")

st.divider()

if st.button("🚪 Выйти"):
    st.session_state.clear()
    st.switch_page("app.py")