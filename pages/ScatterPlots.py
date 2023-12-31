import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

data=pd.read_csv('cluster_0801.csv')

st.subheader('The ScatterPlots of Population data')
  
v_list=['연령대', '총인구수', '1인가구수', '평균 출근 소요시간 평균', '평균 근무시간 평균',
       '소액결재 비사용 인구수', '소액결재 사용횟수 평균', '소액결재 사용금액 평균', '최근 3개월 내 요금 연체 비율',
       '카카오톡 비사용 인구수', 'SNS 사용횟수', '평균 통화량', '평균 문자량', '평균 통화대상자 수',
       '평균 문자대상자 수', '데이터 사용량', '평일 총 이동 횟수', '휴일 총 이동 횟수 평균',
       '집 추정 위치 평일 총 체류시간', '집 추정 위치 휴일 총 체류시간', '평일 총 이동 거리 합계',
       '휴일 총 이동 거리 합계', '지하철이동일수 합계', '게임 서비스 사용일수', '금융 서비스 사용일수',
       '쇼핑 서비스 사용일수', '동영상/방송 서비스 사용일수', '유튜브 사용일수', '넷플릭스 사용일수',
       '배달 서비스 사용일수', '배달_브랜드 서비스 사용일수']

var3 = st.selectbox(label = "Choose a Cluster", options = [0,1,2,3,4,5,6],key=2)
var1 = st.selectbox(label = "Choose a Variable1", options = v_list,key=0)
for i in v_list[:-1]:
  title = f"The ScatterPlots of {var1} and {i} with Cluster {var3}"
  fig1 = px.scatter(data[data['cluster']==var3], x=var1, y=i,title=title)
  fig1.update_traces(marker={'size':10})
  st.plotly_chart(fig1)
