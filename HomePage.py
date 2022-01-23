import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

search = 0
profile = 0

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('HomePageStyle.css')

with st.sidebar:
    st.markdown('<p class="name">Social Stock</p>', unsafe_allow_html=True)
    search = st.button('Search')
    profile = st.button('My Profile')
    Settings = st.button('Settings')
    logout = st.button('Log Out')

# search bar
if search:
    stock = st.text_input('Search')

# portfolio
if profile:
    st.title('User\'s Profile')
    st.write('As of ' + dt_string)
# dummy graph
    chart_data = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['a'])
    st.line_chart(chart_data)
    col1, col2, col3 = st.columns(3)
# dummy portfolio
    with col1:
        st.header("Portfolio")
        st.metric(label="Apple Inc. (AAPL)", value="1020.31", delta="-17.21")
        st.metric(label="S&P 500 (^GSPC)", value="24876.31", delta="-1297.21")

    with col2:
        st.header("Top Movers")