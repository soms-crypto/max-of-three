import streamlit as st

st.title("가장 큰 수 찾기")

# 자연수 입력 함수
def get_natural_number(label, key):
    while True:
        num = st.number_input(label, value=0.0, step=1.0, key=key)
        if num <= 0:
            st.error("자연수만 입력해주세요 (0보다 큰 수)")
            st.stop()
        if num != int(num):
            st.error("정수만 입력해주세요")
            st.stop()
        return int(num)

a = get_natural_number("첫 번째 수", key="a")
b = get_natural_number("두 번째 수", key="b")
c = get_natural_number("세 번째 수", key="c")

if st.button("계산"):
    numbers = [a, b, c]
    if len(numbers) != len(set(numbers)):
        st.error("중복된 값이 있습니다. 서로 다른 수를 입력해주세요.")
        st.stop()

    biggest = max(a, b, c)
    st.success(f"가장 큰 수는 {biggest} 입니다.")
