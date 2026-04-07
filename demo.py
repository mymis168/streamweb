import streamlit as st
import numpy as np
import pandas as pd



def open_file():
    st.write("開啟檔案")
    df = pd.read_csv("C:\\Proj2\\kaggle\\yahooStock.csv")
    st.dataframe(df)
    

st.title("Open File Demo")

st.button("open",icon="🙄", on_click=open_file, help="開啟csv", type="primary")