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

st.session_state.df = data

edited_df = st.data_editor(st.session_state.df, num_rows='dynamic')

st.session_state.df = edited_df

def df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    processed_data = output.getvalue()
    return processed_data

df_xlsx = df_to_excel(st.session_state.df)
st.download_button(label='📥 Download Edited Data as Excel',
                   data=df_xlsx ,
                   file_name= 'edited_data.xlsx')
