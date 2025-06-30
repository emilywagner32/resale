from collections import defaultdict
from pathlib import Path
import sqlite3

import streamlit as st
import altair as alt
import pandas as pd


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title="Resale Inventory Tracker", layout= 'wide')


# -----------------------------------------------------------------------------
# Declare some useful functions.


@st.cache_data(ttl=3600)
def load_data(csv):
    data = pd.read_csv('resale.csv')
    return data
# Load the data
data = load_data('resale.csv')

edited_df = st.data_editor(data)

favorite_command = edited_df.loc[edited_df["SIZE"].idxmax()]["command"]

