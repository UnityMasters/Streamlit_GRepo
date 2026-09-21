import re

import streamlit as st

st.set_page_config(
    page_title="Registration-Form",
    page_icon="🧾",
    layout="centered",
)


def initials(name: str) -> str:
    """Return up to two initials for the account avatar."""
    parts = re.findall(r"[A-Za-z0-9]+", name.strip())
    return "".join(part[0] for part in parts[:2]).upper() or "?"


# Keep the submitted account details while the user navigates between pages.
if "account" not in st.session_state:
    st.session_state.account = None

# A compact, circular account control stays in the top-right of the app.
if st.session_state.account:
    account = st.session_state.account
    st.markdown(
        """
        <style>
        div[data-testid="stPopover"] > button {
            border-radius: 50%;
            width: 44px;
            height: 44px;
            padding: 0;
            background: #2563eb;
            color: white;
            border: 0;
            font-weight: 700;
        }
        div[data-testid="stPopover"] { position: fixed; top: 1rem; right: 1.5rem; z-index: 999; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.popover(initials(account["name"]), use_container_width=False):
        st.subheader("My Account")
        st.write(f"**Name:** {account['name']}")
        st.write(f"**Email:** {account['email']}")
        st.write(f"**Country:** {account['country']}")
        st.caption("Your password is kept private and is not shown here.")
        if st.button("Log out", use_container_width=True):
            st.session_state.account = None
            st.rerun()


if st.session_state.account:
    # This is the page shown after a successful registration.
    account = st.session_state.account
    st.title(f"Welcome, {account['name']}!")
    st.success("Your account has been created successfully.")
    st.write("Use the circular profile button in the top-right corner to view your account details.")
else:
    st.title("Register Before Moving Forward")

    with st.form("rgs_form"):
        name = st.text_input("Name", placeholder="Enter Your Name")
        email = st.text_input("Email", placeholder="Enter Your Email")
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Your Password",
        )
        country = st.selectbox(
            "Country",
            ["India", "USA", "UK", "Canada", "Australia", "Other"],
        )
        submitted = st.form_submit_button("Submit", use_container_width=True)

    if submitted:
        if not name.strip() or not email.strip() or not password:
            st.error("Please complete all fields before submitting.")
        elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email):
            st.error("Please enter a valid email address.")
        else:
            st.session_state.account = {
                "name": name.strip(),
                "email": email.strip(),
                "country": country,
            }
            st.rerun()
