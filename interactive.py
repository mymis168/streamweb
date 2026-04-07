import streamlit as st


st.title("專題呈現")
st.header("除了透過 Power BI呈現資料與分析之外")
st.subheader("亦提供web 方式供使用者瀏覽")


st.write("提供以下查詢方式")
product = st.text_input(label="產品名稱" , value="手機")
st.write(f"使用者輸入的品項: {product}")

sdate = st.date_input("查詢日期",value="today" ,min_value="2026-02-01", 
                                               max_value="today" )
st.write(f"您查詢的範圍開始: {sdate}")

male= st.checkbox("男性", value=False)
female = st.checkbox("女性", value=False)

if male:
    st.write("勾選男生了")

if female:
    st.write("勾選女生了")