import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("男女別年齢別人口", divider="gray")
st.write('年代（年）ごとの男女別年齢（歳）別の人口（人）を表示します。')
df = pd.read_csv('人口ピラミッド_全国（日本）_1920年.csv')
with st.sidebar:
    branch = st.multiselect('年代を選択してください（複数選択可）',
                                df['年代'].unique())
    sex = st.multiselect('男女を指定してください', 
                            df['男女'].unique())
    option = st.segmented_control('表示形式を選択してください',
                  ['表', 'グラフ'])
df = df[df['年代'].isin(branch)]
df = df[df['男女'].isin(sex)]
if option == '表':
    st.dataframe(df, width=800, height=220)
    st.badge("Success", icon=":material/check:", color="green")
elif option == 'グラフ':
    st.line_chart(df.T, width=800, height=450)
    st.badge("Success", icon=":material/check:", color="green")