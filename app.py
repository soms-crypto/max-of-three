import streamlit as st

st.title("가장 큰 수 찾기")

a = st.number_input("첫 번째 수", value=0.0)
b = st.number_input("두 번째 수", value=0.0)
c = st.number_input("세 번째 수", value=0.0)

if st.button("계산"):
    biggest = max(a, b, c)
    st.success(f"가장 큰 수는 {biggest} 입니다.")