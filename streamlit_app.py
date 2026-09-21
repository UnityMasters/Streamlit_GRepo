import streamlit as st

st.set_page_config(
    page_title="Registration-Form",
    page_icon="🧾",
    layout="centered"
)

st.title("Register Before Moving Forward")

with st.form("rgs_form"):
    name = st.text_input("Name",placeholder="Enter Your Name")
    Email = st.text_input("Email",placeholder="Enter Your Email")
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter Your Password"
    )
    country = st.selectbox(
        "Country",
        ["India", "USA", "UK", "Canada", "Australia", "Other"]
    )
    sub = st.form_submit_button(
        "Submit"
    )
