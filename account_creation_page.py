import streamlit as st
import re


with st.form("account_creation_form"):

    st.header("Social Stock Analyzer")
    st.subheader("Create your Account")

    user_name = st.text_input('',placeholder='Username')
    f_name = st.text_input('',placeholder='First name')
    l_name = st.text_input('',placeholder='Last name')
    p_word = st.text_input('',placeholder='Password', type="password")
    st.write("Password guidelines: 8 character minimum, uppercase, lowercase, numbers, and special chars")
    confirm_password = st.text_input('',placeholder='Confirm password', type="password")
    email = st.text_input('',placeholder='E-mail address')
#     store all the input into a dictionary
    input_data = {
                "username" : user_name,
                "first name" : f_name,
                "last name" : l_name,
                "password" : p_word,
                "confirmed password" : confirm_password,
                "email" : email
                }

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

    # add some logic to check valid input
    if submitted:
        for input in input_data.keys():
            if input_data[input] == "" or (input == "confirmed password" and input_data[input] != p_word):
                error = f"Please enter correct {input}."
                error_message = f'<p style="font-family:sans-serif; color:red; font-size: 21px;">{error}</p>'
                st.markdown(error_message, unsafe_allow_html=True)

        if IsValidPassword(p_word) == False:
            error = "Password doesn't follow the password guidelines. Please enter a stronger password."
            error_message = f'<p style="font-family:sans-serif; color:red; font-size: 21px;">{error}</p>'
            st.markdown(error_message, unsafe_allow_html=True)

    st.write("Have an account? Sign In")




