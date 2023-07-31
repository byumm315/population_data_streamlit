import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="Home"
)
st.title('Population Data Clustering') #홈페이지 제목추가
st.header('Find the features of Cluster')
st.image('https://img.jagranjosh.com/images/2022/July/1172022/Compress_world_Population.webp')
data=pd.read_csv('cluster_0801.csv')
st.write(data.head(20))
