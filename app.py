import streamlit as st
import pandas as pd
import plotly.express as px

st.title('男女別年齢別人口')
df = pd.read_csv('人口ピラミッド_全国（日本）_1920年.csv')