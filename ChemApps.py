import streamlit as st

# タイトル
st.set_page_config(page_title="ChemApps", page_icon=":bar_chart:", )


# sidebar
uv_vis = st.Page(page="contents/uv-vis.py", title="UV-vis | JASCO .txt > xlsx", icon="📊")
ir = st.Page(page="contents/ir.py", title="IR  | JASCO .txt > xlsx", icon="📊")
gausslog = st.Page(page="contents/gausslog.py", title="DFT | GaussLog", icon="📄")
pg = st.navigation([uv_vis, ir, gausslog])
pg.run()
