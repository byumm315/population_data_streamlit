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
import matplotlib as mpl
st.subheader(set(sorted([f.name for f in mpl.font_manager.fontManager.ttflist])))
