import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    font_dirs = ["C:/Users/tyumi"]
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)
    

fontRegistered()
fontNames = [f.name for f in fm.fontManager.ttflist]
st.subheader(fontnames)
