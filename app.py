# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:39:27 2021

@author: LocalAdmin
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache
def load_data(nrows = 1000):
    df = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv',
                      nrows = 1000)
    return df

section = st.sidebar.radio('Application Section', ['Data Explorer', 
                                                   'Model Explorer'])
if section == 'Data Explorer':
    nrows = st.sidebar.number_input("Number of Rows to Load", min_value = 1000,
                            max_value = 10000, step = 1000)
    
    df = load_data(nrows)
    
    
    x_axis = st.sidebar.selectbox('Choose Your X-Axis Category', df.select_dtypes(include=np.object).columns)
    
    y_axis = st.sidebar.selectbox('Choose Your Y-Axis Category', df.select_dtypes(include=np.number).columns)
    
    chart_type = st.sidebar.selectbox('Choose Your chart type', ['Table', 'Line','Bar','Strip'])
    
    @st.cache
    def create_grouping(x_axis, y_axis):
        grouping = df.groupby(x_axis)[y_axis].mean()
        return grouping
    
    grouping = create_grouping(x_axis, y_axis)
    
    st.write(df)
    
    st.title("Grouped data")
    
    if chart_type == 'line':
        # make a line chart
        st.line_chart(grouping)
    elif chart_type == 'bar':
        # make a bar chart
        st.bar_chart(grouping)
    elif chart_type == 'table':
        # make a table
        st.write(grouping)
    else:
        st.plotly_chart(px.strip(df[[x_axis, y_axis]], x=x_axis, y=y_axis))
        
else:
 category = st.sidebar.selectbox('Chose your category', df['category'].unique())   
 
 subcategory = st.sidebar.selectbox('Chose your subcategory', df['main_category'].unique())  




