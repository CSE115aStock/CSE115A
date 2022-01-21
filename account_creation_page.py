import streamlit as st


with st.form("account_creation_form"):

    st.header("Social Stock Analyzer")
    st.subheader("Create your Account")

    Username = st.text_input('',placeholder='Username')
    Firstname = st.text_input('',placeholder='Firstname')
    Lastname = st.text_input('',placeholder='Lastname')
    Password = st.text_input('',placeholder='Password')
    Confirm_password = st.text_input('',placeholder='Confirm password')
    Email = st.text_input('',placeholder='E-mail address')

    submitted = st.form_submit_button("Sign Up")
    if submitted:
        username = Username
        password = Password
        email = Email

    st.write("Have an account? Sign In")

