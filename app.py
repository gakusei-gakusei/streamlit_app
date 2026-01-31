import streamlit as st
import pandas as pd
import plotly.express as px

st.title('男女別年齢別人口')
st.write('年代ごとの男女別年齢別の人口を表示します。')
df = pd.read_csv('人口ピラミッド_全国（日本）_1920年.csv')
with st.sidebar:
    branch = st.multiselect('年代を選択してください（複数選択可）',
                                df['時点'].unique())
    year = st.multiselect('年齢を指定してください', 
                            df['年齢区分'].unique())
    option = st.radio('表示形式を選択してください',
                  ['表', 'グラフ'])
