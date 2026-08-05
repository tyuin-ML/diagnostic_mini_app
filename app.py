
import streamlit as st

st.title("Быстрый отчет о диагностике/замене ✍")

worktypearr = {"Замена узла":1, "Диагностика":0}
worktype = st.selectbox('Выберете тип проведенных работ', list(worktypearr))

pointnumber = st.number_input("**Номер узла**", min_value = 1, max_value = 9999, value = None, step = 1, placeholder = "Введите индивидуальный номер, указаный на датчике")



workreport = st.text_area("**Кратко опишите результат проведенных работ**", placeholder ="Расскажите что было заменено или какая проблема была диагностирована")

if worktype == "Диагностика":
    agree = st.checkbox("Проблема устранена")


st.write(pointnumber)
st.write(workreport)
