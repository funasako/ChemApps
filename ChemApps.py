import streamlit as st

# タイトル
st.set_page_config(page_title="ChemApps", page_icon=":bar_chart:", )

# sidebar
uv-vis = st.Page(page="pages/01_uv-vis.py", title="UV-vis to Excel", icon="📊")
ir = st.Page(page="pages/02_ir.py", title="IR to Excel", icon="📊")
gausslog = st.Page(page="pages/03_gausslog.py", title="GaussLog", icon="📄")
pg = st.navigation([uv-vis, ir, gausslog])
pg.run()

# コンテンツ
st.title("ChemApps")
st.write("左のメニューからアプリを選択")
