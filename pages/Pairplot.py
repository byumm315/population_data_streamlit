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

col={}
for i in list(data.columns):
  col[i]=v_list[i]
data.rename(columns=col,inplace=True)

data['cluster']=list(map(str,data['cluster']))
st.subheader('Part1')
data_1=data[v_list[2:7]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)

st.subheader('Part2')
data_1=data[v_list[7:12]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)

st.subheader('Part3')
data_1=data[v_list[12:17]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)

st.subheader('Part4')
data_1=data[v_list[17:22]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)

st.subheader('Part5')
data_1=data[v_list[22:27]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)

st.subheader('Part6')
data_1=data[v_list[27:-2]]
data_1['cluster']=data['cluster']
fig1 = px.scatter_matrix(data_1,color='cluster',height=1000, width=1000)
fig1.update_traces(marker={'size':3})
st.plotly_chart(fig1)
