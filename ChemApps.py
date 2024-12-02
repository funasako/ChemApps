import streamlit as st

uv-vis = st.Page(page="pages/01_uv-vis.py", title="UV-vis to Excel", icon="📊")
ir = st.Page(page="pages/02_ir.py", title="IR to Excel", icon="📊")
gausslog = st.Page(page="pages/03_gausslog.py", title="GaussLog", icon="📄")
pg = st.navigation([top_page, my_profile, about])
pg.run()

# タイトル等
st.title("ChemApps")
st.write("左のメニューからアプリを選択")
