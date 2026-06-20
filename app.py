import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data
df = pd.read_csv("house_data.csv")

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

st.title("🏠 House Price Prediction")

area = st.number_input("Enter House Area", min_value=50)

if st.button("Predict Price"):
    prediction = model.predict([[area]])
    st.success(f"Predicted Price: ₹ {int(prediction[0]):,}")