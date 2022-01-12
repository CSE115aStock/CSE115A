import argparse
import os

import numpy as np
import pandas as pd
import plotly.express as px

import streamlit as st


if __name__ == "__main__":
    st.set_page_config(
        page_title="StockSocial",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.title("Stock Viz")
