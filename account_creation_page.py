import streamlit as st
import re


with st.form("account_creation_form"):

    st.header("Social Stock Analyzer")
    st.subheader("Create your Account")

    user_name = st.text_input('',placeholder='Username')
    f_name = st.text_input('',placeholder='Firstname')
    l_name = st.text_input('',placeholder='Lastname')
    password = st.text_input('',placeholder='Password', type="password")
    st.write("Password guidelines: 8 character minimum, uppercase, lowercase, numbers, and special chars")
    confirm_password = st.text_input('',placeholder='Confirm password', type="password")
    email = st.text_input('',placeholder='E-mail address')
    submitted = st.form_submit_button("Sign Up")

    # function used to check if a password contains uppercase, lowercase, special character & numeric value
    def IsValidPassword(str):

        regex = ("^(?=.*[a-z])(?=." +
                     "*[A-Z])(?=.*\\d)" +
                     "(?=.*[-+_!@#$%^&*., ?]).+$")

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if (len(str) < 8):
            return False

        # return true if string matches ReGex
        if (re.search(p, str)):
            return True
        else:
            return False

    if submitted:
        if user_name == "":
            st.write("Please enter Username.")
        elif f_name == "":
            st.write("Please enter Firstname.")
        elif l_name == "":
            st.write("Please enter Lastname.")
        elif IsValidPassword(password) == False:
            st.write("Password doesn't follow the password guidelines. Please enter stronger password.")
        elif confirm_password == "":
            st.write("Please confirm password.")
        elif password != confirm_password:
            st.write("Password and confirm_password are different.")
        elif email == "":
            st.write("Please enter email.")

    st.write("Have an account? Sign In")




