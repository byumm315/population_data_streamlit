# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm
font_file=fm.findSystemFonts(fontpaths=os.getcwd())
fm.fontManager.addfont(font_file[0])
fm._load_fontmanager(try_read_cache=False)
fontNames = [f.name for f in fm.fontManager.ttflist]
st.subheader(fontNames)

plt.rc('font', family=fontNames)
tips = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
ax.set_title("한글 테스트")
st.pyplot(fig)
st.dataframe(tips)
