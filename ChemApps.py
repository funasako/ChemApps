import streamlit as st

# タイトル
st.set_page_config(page_title="ChemApps", page_icon=":test_tube:", )

# マルチページモードフラグを設定
st.session_state['multi_page'] = True  # フラグをTrueに設定

# sidebar
uv_vis = st.Page(page="contents/uv-vis.py", title="UV-vis | JASCO/HITACHI txt to xlsx", icon="📊")
ir = st.Page(page="contents/ir.py", title="Infrared | JASCO txt to xlsx", icon="📊")
gausslog = st.Page(page="contents/gausslog.py", title="DFT | GaussLog", icon="📄")
pg = st.navigation([uv_vis, ir, gausslog])
pg.run()
