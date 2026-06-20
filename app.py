import streamlit as st
import pandas as pd

st.title("House Price Prediction")

df = pd.read_csv("house_data.csv")

st.success("CSV loaded successfully!")
st.write(df.head())
