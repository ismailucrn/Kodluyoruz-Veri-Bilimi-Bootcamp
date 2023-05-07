import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Hello World!")

df = pd.read_csv("house_price.csv")

st.table(df.head())

st.line_chart(df["SalePrice"])

tilki = st.radio("head or tail", ("head", "tail"))

if tilki == "head":
    st.bar_chart(df["SalePrice"])   

else:
    st.bar_chart(df["LotArea"])   

fig = px.histogram(df, x="SalePrice", nbins=50, title="Sale Price Distribution")
st.plotly_chart(fig)

list = df.columns.tolist()

a = st.selectbox("Select Column", list)

if df[a].dtype == "object":
    st.bar_chart(df[a])
else:
    st.line_chart(df[a])