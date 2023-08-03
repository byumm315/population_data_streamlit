import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc,rcParams

data=pd.read_csv('cluster_0801.csv')

st.subheader('The Pairplot of Poulation data')
  
v_list=list(data.columns)

for i in range(len(v_list)):
    v_list[i]=v_list[i].replace('평균','')
    v_list[i]=v_list[i].strip()

data_1=data.drop('cluster',axis=1)
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=6000, width=6000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)
