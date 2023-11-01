import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The EDA App**
            
This is the **EDA App** created in Streamlit using the **pandas-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by [Will Torres](https://linkedin.com/in/torreswill)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    example_csv_url = "https://raw.githubusercontent.com/torrwill/eda_streamlit/main/CarPrice_Assignment.csv"
    st.sidebar.markdown(f"[Example CSV input file]({example_csv_url})")

# Pandas Profiling Report
@st.cache_data
def read_uploaded_csv():
    csv = pd.read_csv(uploaded_file)
    return csv

if uploaded_file is not None:
    df = read_uploaded_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    button_label = 'Press to Reload Example Dataset' if st.button('Press to Reload Example Dataset') else 'Press to use Example Dataset'
    if button_label:
        @st.cache_data
        def load_data():
            a = pd.read_csv(example_csv_url, index_col=0)
            return a

        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

# User Instructions
st.sidebar.markdown('''
### Instructions
- Upload a CSV file for exploratory data analysis.
- For example data, use the provided [Example CSV input file]({example_csv_url}).
''')
