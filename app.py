import streamlit as st
import time

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(grey,white,black);
        background-image: url("https://share.google/images/Y0jDbKzgUtaLNnuD9")
        background-size: cover;
        font-family: cursive, "sans-serif", script;
        color: red;
    }
    .stButton>button {
            background-color: black;
            color: white;
            border-radius: 10px;
            font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)


if 'page' not in st.session_state:
    st.session_state.page = 'home'


if st.session_state.page == 'home':
    st.title("Welcome my nigga!!")
    name = st.text_input("Enter your name:")
    nickname = st.text_input("who be this one, enter my nickname joor")

    if st.button("Click me Oga"):
        if name.strip() == "":
            st.warning("Enter your name, you no dey see me")
        elif nickname.strip() != "Raphiki":
            st.error("warning answer you no sabi book. Try again joor") 
        else:
            st.session_state.page = 'dashboard'
            st.rerun()

elif st.session_state.page == 'dashboard':
    msg1 = st.empty()
    msg2 = st.empty()

    time.sleep(0.5)
    msg1.write("sabi pekin na only you waka come.")

    time.sleep(1.5)
    msg2.write("normally on a rainy night like this, we gats use umbrella guide from the gaze of the sun. Anyways i just wan wish you Happy newyear Fam. Abeg make God run em for us this year make we guide,make we self throw steps for tiktok. Amen")

    if st.button("incase your eye dey pain click make you go back the first page"):
        st.session_state.page = 'home'
        st.rerun()
