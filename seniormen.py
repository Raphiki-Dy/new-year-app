import streamlit as st
import time

st.markdown("""
    <style>
    .stApp {
        background: grey;
        background-image: url("https://share.google/images/Y0jDbKzgUtaLNnuD9");
        background-size: cover;
        font-family: cursive, "sans-serif", script;
        color: lightblue;
    }
    .stButton>button {
            background-color: white;
            color: black;
            border-radius: 10px;
            font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)


if 'page' not in st.session_state:
    st.session_state.page = 'home'


if st.session_state.page == 'home':
    st.title("Ehn Welcome my people!!")
    name = st.text_input("Enter your name:")
    nickname = st.text_input("Enter my English name ")

    if st.button("Click me"):
        if name.strip() == "":
            st.warning("please enter your name")
        elif nickname.strip() != "Destiny":
            st.error("this one touch me, please try again!") 
        else:
            st.session_state.name = name
            st.session_state.page = 'dashboard'
            st.rerun()

elif st.session_state.page == 'dashboard':
    msg1 = st.empty()
    msg2 = st.empty()
    msg3 = st.empty()
    msg4 = st.empty()
    msg5 = st.empty()

    time.sleep(0.5)
    msg1.write(f"Hello {st.session_state.name}!")
    time.sleep(1.0)
    msg2.write("Oya welcome Senior Man/Lady.")
    time.sleep(1.0)
    msg3.write("before you continue just take small time say God thank you for bringing me this far.")
    time.sleep(2.0)
    msg4.write("My dear family, as we enter this new year, make una remember say no be only you waka come, God don carry all of us come this far together with plenty blessings, love, and joy!  My wonderful people i wish una Happy New Year full of favor, good health, breakthroughs and ego(money)! I love una scatter!")

    time.sleep(2.0)
    msg5.write("Raphiki")
    if st.button("this button go just take you go back the first page"):
        st.session_state.page = 'home'
        st.rerun()
