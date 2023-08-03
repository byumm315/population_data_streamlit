# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm
f = [f.name for f in fm.fontManager.ttflist]

st.subheader(f)
