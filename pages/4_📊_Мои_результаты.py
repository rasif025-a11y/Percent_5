import streamlit as st
if "role" not in st.session_state:
    st.switch_page("app.py")
st.title("📊 Мои результаты")

score = st.session_state.get("score", 0)
attempts = st.session_state.get("attempts", 0)

name = st.session_state.get("user", "Ученик")

st.subheader(f"👤 {name}")

st.write(f"✅ Правильных ответов: **{score}**")
st.write(f"📝 Всего попыток: **{attempts}**")

if attempts > 0:

    percent = round(score / attempts * 100, 1)

    st.write(f"🎯 Успешность: **{percent}%**")

    st.progress(percent / 100)

    if percent >= 90:
        st.success("🏆 Отличный результат!")

    elif percent >= 70:
        st.info("👍 Хорошая работа!")

    elif percent >= 50:
        st.warning("📚 Нужно ещё немного потренироваться.")

    else:
        st.error("💪 Не сдавайтесь! Всё получится!")

else:
    st.info("Пока нет результатов.")
    