import streamlit as st
import pandas as pd
from database import get_results
import streamlit as st

if "role" not in st.session_state:
    st.switch_page("app.py")

if st.session_state["role"] != "teacher":
    st.warning("🛑 Страница доступна только учителю.")
    st.stop()
st.title("📊 Статистика учеников")

# Получение данных
data = get_results()

if len(data) == 0:
    st.info("Пока нет результатов.")
    st.stop()

# Создаем таблицу
df = pd.DataFrame(
    data,
    columns=[
        "👤 Ученик",
        "✅ Правильных",
        "❌ Попыток"
    ]
)

# Добавляем процент успешности
df["📈 Процент (%)"] = round(
    df["✅ Правильных"] /
    df["❌ Попыток"] * 100,
    1
)

# Поиск ученика
search = st.text_input("🔍 Поиск ученика")

if search:
    df = df[
        df["👤 Ученик"].str.contains(
            search,
            case=False
        )
    ]

st.subheader("📋 Таблица результатов")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# Общая статистика
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍🎓 Учеников",
        len(df)
    )

with col2:
    st.metric(
        "🎯 Средний прогресс",
        f"{round(df['📈 Процент (%)'].mean(),1)}%"
    )

with col3:
    best = df.loc[df["📈 Процент (%)"].idxmax()]

    st.metric(
        "🏆 Лучший ученик",
        best["👤 Ученик"]
    )

st.divider()

st.subheader("📈 Диаграмма успеха")

chart = df.set_index("👤 Ученик")["📈 Процент (%)"]

st.bar_chart(chart)

st.divider()

st.subheader("🥇 Топ-3 учеников")

top = df.sort_values(
    by="📈 Процент (%)",
    ascending=False
).head(3)

st.table(top)

st.divider()

csv = df.to_csv(
    index=False
).encode("utf-8-sig")

st.download_button(
    label="📥 Скачать статистику",
    data=csv,
    file_name="Статистика_учеников.csv",
    mime="text/csv"
)
