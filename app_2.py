# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm

path = '/usr/share/fonts/truetype/nanum/NanumGothic_Coding.ttf' # fontlist에 있던 경로입니다
font_name = fm.FontProperties(fname=path).get_name()
rc('font', family=font_name)
st.subheader(font_name)
