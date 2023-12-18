import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Upload Dataset',
    layout="wide",
    initial_sidebar_state="expanded"
)

if "dataset_file" not in st.session_state:
    st.session_state.dataset_file = None
if "dataset" not in st.session_state:
    st.session_state.dataset = None

dataset_file = st.file_uploader(".parquet only for now")
st.session_state.dataset_file = dataset_file

if st.session_state.dataset_file is None:
    st.write("No Dataset yet")
else:
    # read data
    df = pd.read_parquet(st.session_state.dataset_file)
    st.session_state.dataset = df
    st.write(df.head())

