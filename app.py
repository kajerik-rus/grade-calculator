import streamlit as st

total = 0
total1 = 0
grades = []
weigths = []

st.title("Калькулятор средневзвешенного балла")

count = st.number_input(
    "Сколько у тебя оценок?",
    min_value=0,
    max_value=100,
    value=2,
    step=1
)

if count <= 0:
    st.error("Нет такого количества оценок!")
elif count <= 1:
    st.info("Зачем тебе тогда средний балл?")
else:
    with st.form("calculator"):
        for i in range(int(count)):
            st.subheader(f"Оценка №{i + 1}")

            grade = st.text_input(
                "Какая у тебя оценка?",
                key=f"grade_{i}"
            )

            weigth = st.text_input(
                "Какой её вес?",
                key=f"weight_{i}"
            )

            grades.append(grade)
            weigths.append(weigth)

        submitted = st.form_submit_button("Рассчитать")

    if submitted:
        grades1 = []
        weigths1 = []
        errors = []

        for i in range(len(grades)):
            try:
                grade = int(grades[i])
                weigth = int(weigths[i])
            except ValueError:
                errors.append(
                    f"Оценка №{i + 1}: нужно ввести целые числа!"
                )
                continue

            if grade < 2 or grade > 5:
                errors.append(
                    f"Оценка №{i + 1}: нет такой оценки!"
                )
            elif weigth < 10 or weigth > 40:
                errors.append(
                    f"Оценка №{i + 1}: нет такого веса!"
                )
            else:
                grades1.append(grade)
                weigths1.append(weigth)

        if errors:
            for error in errors:
                st.error(error)
        else:
            for i in range(len(grades1)):
                total = weigths1[i] * grades1[i] + total

            total1 = sum(weigths1)

            st.write("Конец списка.")
            st.success(
                f"Средняя оценка: {round(total / total1, 2)}"
            )
