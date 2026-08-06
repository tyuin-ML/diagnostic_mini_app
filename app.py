from datetime import datetime
import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Быстрый отчет о диагностике/замене ✍")

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

if worktype == "Диагностика":
    resolved = st.checkbox("Проблема устранена")
else:
    resolved = None

# --- ОБНОВЛЕННЫЙ БЛОК: Выбор даты и часа ---
st.write("**Дата и время проведения работ**")
use_current_time = st.checkbox("Использовать текущее время (Сейчас)", value=True)

now = datetime.now()

if use_current_time:
    report_date = now.date()
    report_hour = now.hour
    st.info(f"Будет сохранено: {report_date.strftime('%d.%m.%Y')} в {report_hour}:00")
else:
    col1, col2 = st.columns(2)
    with col1:
        report_date = st.date_input("Выберите дату", value=datetime.today())
    with col2:
        # Удобный ползунок для выбора часа вместо выпадающего списка
        report_hour = st.time_input("Выберите час", value = None)

# Формируем итоговую дату с точностью до часа (минуты и секунды сбрасываем в 00:00)
final_datetime = f"{report_date} {report_hour:02d}:00:00"
# --------------------------------------------

if st.button("Отправить отчет"):
    if not workreport:
        st.error("Пожалуйста, заполните описание результатов работ!")
    elif pointnumber is None:
        st.error("Пожалуйста, укажите номер узла!")
    else:
        st.session_state.fullreportarr = {
            "datetime": final_datetime,
            "worktype": worktype,
            "worktype_id": worktypearr[worktype],
            "pointnumber": pointnumber,
            "workreport": workreport,
            "problem_resolved": resolved
        }
        st.success("Отчет успешно сформирован!")

if st.session_state.fullreportarr is not None:
    st.write("### Текущий сохраненный отчет:")
    st.json(st.session_state.fullreportarr)


footer {visibility: hidden;}