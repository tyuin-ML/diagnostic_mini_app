import streamlit as st

st.title("Быстрый отчет о диагностике/замене ✍")

# Переносим инициализацию session_state в самое начало скрипта
if "fullreportarr" not in st.session_state:
    st.session_state.fullreportarr = None

worktypearr = {"Замена узла": 1, "Диагностика": 0}
worktype = st.selectbox('Выберете тип проведенных работ', list(worktypearr))

pointnumber = st.number_input(
    "**Номер узла**",
    min_value=1,
    max_value=9999,
    value=None,
    step=1,
    placeholder="Введите индивидуальный номер, указаный на датчике"
)

workreport = st.text_area(
    "**Кратко опишите результат проведенных работ**",
    placeholder="Расскажите что было заменено или какая проблема была диагностирована"
)

# Инициализируем значение чекбокса по умолчанию (для "Замена узла" оно будет None или False)
resolved = None

if worktype == "Диагностика":
    resolved = st.checkbox("Проблема устранена")

# Кнопку и логику отправки лучше вынести из-под условия text_area,
# а проверку на заполненность сделать внутри нажатия кнопки
if st.button("Отправить отчет"):
    if not workreport:
        st.error("Пожалуйста, заполните описание результатов работ!")
    elif pointnumber is None:
        st.error("Пожалуйста, укажите номер узла!")
    else:
        # Формируем итоговый словарь
        st.session_state.fullreportarr = {
            "worktype": worktype,
            "worktype_id": worktypearr[worktype], # Добавили ID типа работы (0 или 1)
            "pointnumber": pointnumber,
            "workreport": workreport,
            "problem_resolved": resolved # Сюда запишется True/False для диагностики и None для замены
        }
        st.success("Отчет успешно сформирован!")

# Вывод результата всегда находится вне условий кнопок, чтобы данные не исчезали
if st.session_state.fullreportarr is not None:
    st.write("### Текущий сохраненный отчет:")
    st.json(st.session_state.fullreportarr) # st.json выглядит аккуратнее для словарей
