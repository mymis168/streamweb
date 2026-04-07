import streamlit as st
import numpy as np
import pandas as pd






st.title("Streamlit Button 展示")

click1 = st.button("這是Button-1" , key="btnDemo1", type="primary", icon="🤏")
click2 = st.button("這是Button-2" , key="btnDemo2", type="secondary",icon="💂‍♂️", icon_position="right")
if click1:
    st.write("button-1 點擊了")

if click2:
    st.header("button-2 clicked !!")    

def open_csv():
    st.write("開啟 C:\\Proj2\\kaggle\\sales_csv.csv")
    df = pd.read_csv("C:\\Proj2\\kaggle\\sales_csv.csv")
    st.dataframe(df)


st.button("開啟Yahoo股價檔案", on_click=open_csv ,icon="⏱️" , type="tertiary") 

