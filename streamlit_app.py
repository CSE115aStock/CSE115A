import argparse
import os
import sys
import psycopg2

import numpy as np
import pandas as pd
import plotly.express as px
from UserDataAccess import AddUser

import streamlit as st



if __name__ == "__main__":
    st.set_page_config(
        page_title="StockSocial",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.title("Stock Viz")

    try:
        conn = psycopg2.connect(**st.secrets["postgres_userdb"])     
    except Exception as e:
        print("Database connection failed due to {}".format(e))

    """
    #Test adding user to db
    f_name = st.text_area("Enter first name:")
    l_name = st.text_area("Enter last name:")
    email = st.text_area("Enter email:")
    username = st.text_area("Enter username:")
    password = st.text_area("Enter password:")

    create = st.button("Create Account")

    if create:
        AddUser(conn,f_name,l_name,email,username,password)

        #check if added succesfully to user db
        cursor = conn.cursor()
        cursor.execute("SELECT * from users")
        all_users = cursor.fetchall()
        print(all_users)
        conn.close()
    """
    
    




