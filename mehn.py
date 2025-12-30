import streamlit as st
import time

st.markdown("""
    <style>
    .stApp {
        background: grey;
        background-image: url("https://share.google/images/Y0jDbKzgUtaLNnuD9");
        background-size: cover;
        font-family: cursive, "sans-serif", script;
        color: blue;
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
    st.title("Welcome my nigga!!")
    name = st.text_input("Enter your name:")
    nickname = st.text_input("who be this one, enter my nickname joor")

    if st.button("Click me Oga"):
        if name.strip() == "":
            st.warning("Enter your name abeg no let me talk")
        elif nickname.strip() != "Raphiki":
            st.error("wrong answer you no sabi book. Try again joor") 
        else:
            st.session_state.name = name
            st.session_state.page = 'dashboard'
            st.rerun()

elif st.session_state.page == 'dashboard':
    msg1 = st.empty()
    msg2 = st.empty()
    msg3 = st.empty()

    time.sleep(0.5)
    msg1.write(f"Hello {st.session_state.name}!")
    time.sleep(1.0)
    msg2.write("sabi pekin na only you waka come.")

    time.sleep(1.5)
    msg3.write("normally on a rainy night like this, we gats use umbrella guide from the gaze of the sun. Anyways i just wan wish you Happy newyear Fam. I pray this year go bring us more Favour and less Amaka(no think that part). Abeg make God run em for us this year make we guide,make we self throw steps for tiktok. Amen")

    if st.button("incase your eye dey pain click make you go back the first page"):
        st.session_state.page = 'home'
        st.rerun()
