import streamlit as st

# タイトル
st.set_page_config(page_title="ChemApps", page_icon=":test_tube:", )


# sidebar
uv_vis = st.Page(page="contents/uv-vis.py", title="UV-vis | JASCO .txt to xlsx", icon="📊")
ir = st.Page(page="contents/ir.py", title="Infrared | JASCO .txt to xlsx", icon="📊")
gausslog = st.Page(page="contents/gausslog.py", title="DFT | GaussLog", icon="📄")
pg = st.navigation([uv_vis, ir, gausslog])

# コメントの追加
st.sidebar.markdown("---")  # 区切り線を挿入
st.sidebar.write("各ツールはJASCOデータの変換と分析をサポートします。")

pg.run()
