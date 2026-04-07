import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

start = st.date_input("日期", value="today", min_value="2026-01-01", max_value="today")
st.write(f"選擇:  {start}")

def alert():
    st.toast("button trigger",duration="short")

st.button("ok", on_click=alert)
st.header("Line Chart demo")
st.subheader("各業務業績")
st.line_chart(df)

