import streamlit as st

# タイトル
st.set_page_config(page_title="ChemApps", page_icon=":test_tube:", )

# サイドバー
st.sidebar.title("ページナビゲーション")
uv_vis = st.sidebar.button("📊 UV-vis | JASCO .txt to xlsx")
ir = st.sidebar.button("📊 Infrared | JASCO .txt to xlsx")
gausslog = st.sidebar.button("📄 DFT | GaussLog")

# コメントの追加
st.sidebar.markdown("---")  # 区切り線を挿入
st.sidebar.write("各ツールはJASCOデータの変換と分析をサポートします。")

# ボタンの動作設定
if uv_vis:
    st.experimental_set_query_params(page="uv-vis")
elif ir:
    st.experimental_set_query_params(page="ir")
elif gausslog:
    st.experimental_set_query_params(page="gausslog")
