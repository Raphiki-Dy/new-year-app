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
    st.title("Ehn Welcome Mummy GO!!")
    name = st.text_input("Enter your name:")
    nickname = st.text_input("Enter my nickname ")

    if st.button("Click me"):
        if name.strip() == "":
            st.warning("please enter your name")
        elif nickname.strip() != "Raphiki":
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
    msg2.write("Welcome Chef D.")
    time.sleep(1.0)
    msg3.write("before you continue just take small time say God thank you for bringing me this far.")
    time.sleep(2.0)
    msg4.write("Daniella Briade Biobele Sena, hmm this seems too much anyways D you have been such a blessing to me and everyone around you(especially the behind the scene acts), anyways for my verison of Daniella i wish you a Happy new year filled with love, joy, good health, and success in all you do")

    time.sleep(2.0)
    msg5.write("Raphiki")
    if st.button("click me if you still ....."):
        st.session_state.page = 'home'
        st.rerun()
