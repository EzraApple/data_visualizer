import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Visualize Features',
    layout="wide",
    initial_sidebar_state="expanded"
)

if "features" not in st.session_state:
    st.session_state.features = []
if "dataset" not in st.session_state:
    st.session_state.dataset = None


def plot_features(standardize, smoothing, differential, run_id):
    data = st.session_state.dataset
    data = data[data["run_id"]==run_id][st.session_state.features]
    if standardize:
        data = (data - data.mean())/data.std()
    if smoothing:
        window_size = st.slider("Smoothing Window Size", 1, 500, help="Smooths by mean value over window_size")
        data = data.rolling(window=window_size).mean().dropna()
    if differential:
        data = data.diff().dropna()
    st.line_chart(data=data, y=st.session_state.features, height=600)


if st.session_state.dataset is None:
    st.write("Please Upload a Dataset First")
else:
    col1, col2 = st.columns(2)
    with col1:
        features = st.multiselect("Features to plot", st.session_state.dataset.columns)
    with col2:
        run_id = st.selectbox("Select Run", st.session_state.dataset["run_id"].unique())
    st.session_state.features = features
    col1, col2, col3 = st.columns(3)
    with col1:
        standardize = st.checkbox("Standardize Features", help="x = (x-mean)/std")
    with col2:
        smoothing = st.checkbox("Apply Smoothing", help="Smooths by mean value over window_size")
    with col3:
        differential = st.checkbox("Convert to Differential", help="Turns datapoints into differences instead of values")

    plot_features(standardize, smoothing, differential, run_id)
