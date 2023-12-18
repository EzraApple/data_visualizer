import streamlit as st
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
    page_title='Compare Features',
    layout="wide",
    initial_sidebar_state="expanded"
)

if "features" not in st.session_state:
    st.session_state.features = []
if "dataset" not in st.session_state:
    st.session_state.dataset = None

if st.session_state.dataset is None:
    st.write("Please Upload a Dataset First")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        y_axis = st.multiselect("Y Axis", st.session_state.dataset.columns, help="Please only select 1 feature :,(")
    with col2:
        x_axis = st.multiselect("X Axis", st.session_state.dataset.columns, help="Please only select 1 feature :,(")
    with col3:
        run_id = st.selectbox("Select Run", st.session_state.dataset["run_id"].unique())
    dataset = st.session_state.dataset[st.session_state.dataset["run_id"]==run_id]
    heatmap = st.checkbox("Apply Heatmap")
    if x_axis and y_axis:
        if heatmap:
            color_by = st.selectbox("Color By", st.session_state.dataset.columns.values.tolist(), index=None)
            fig = px.scatter(dataset, x=x_axis[0], y=y_axis[0], color=color_by, height=600)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.scatter_chart(data=dataset, x=x_axis[0], y=y_axis[0], height=600)

