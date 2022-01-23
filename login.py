import os
import streamlit as st
from datetime import datetime, timedelta
from DataAccess import UserDB
class Login:
    def __init__(self):
        self.user = False
        self.username = None
        self.passowrd = None
    def loginScreen(self):
        login_form = st.form('Login')
        self.username = login_form.text_input('Username')
        self.password = login_form.text_input('Password',type='password')
        submit = login_form.form_submit_button('Login')
        if submit:
            if self.username and self.password:
                try:
                    conn = psycopg2.connect(**st.secrets["postgres_userdb"])
                    User = UserDB()
                    self.user = User.AuthenticateUser(conn, self.username,self.password)
                except Exception as e:
                        st.warning('Password or Username was Incorrect')
            else:
                st.warning('Please enter your username and password')
if __name__ == '__main__':
    login= Login()
    login.loginScreen()
    
    
