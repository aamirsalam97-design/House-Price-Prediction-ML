import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("house_data.csv")

# Features and Target
X = df[["Area"]]
y = df["Price"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# User Input
area = int(input("Enter House Area: "))

# Prediction
prediction = model.predict(pd.DataFrame([[area]], columns=["Area"]))

print("Predicted House Price =", int(prediction[0]))

# Graph
plt.scatter(df["Area"], df["Price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction")
plt.show()