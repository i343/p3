import streamlit as st

st.title("Чат-бот")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Вы:", "")

if user_input:
    st.session_state.history.append(("Вы", user_input))
    response = f"Бот: {user_input[::-1]}"  # простой ответ
    st.session_state.history.append(("Бот", response))

for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")
