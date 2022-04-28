# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:01:31 2022

@author: korin
"""

#packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#dataset
@st.cache
def load_data():
    df = pd.read_csv('C:/Users/korin/OneDrive/Documents/GitHub/no-show-appointments-project/no_show_may_2016.csv')
    return df
df = load_data()
#exploration
df.info()
print(df.describe())

