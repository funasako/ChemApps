import streamlit as st

# タイトル等
st.set_page_config(page_title="ChemApps", page_icon=":bar_chart:", )
st.title("ChemApps")
st.write("左のメニューからアプリを選択")

with st.sidebar:
    st.page_link("pages/01_uv-vis.py", label="UV-vis to Excel", icon="📊")
    st.page_link("pages/02_ir.py", label="IR to Excel", icon="📊")
    st.page_link("pages/03_gausslog.py", label="GaussLog", icon="📄")


