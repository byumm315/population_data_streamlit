# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm

# 설치된 폰트 출력
font_list = [font.name for font in fm.fontManager.ttflist]
st.subheader(font_list)
