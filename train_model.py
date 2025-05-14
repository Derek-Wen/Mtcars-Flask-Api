import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("mtcars.csv")

if "model" in df.columns:
    df = df.drop("model", axis=1)

X = df.drop("mpg", axis=1)
y = df["mpg"]

model = LinearRegression().fit(X, y)

joblib.dump(model, "mtcars_model.pkl")
print("Model trained and saved to mtcars_model.pkl")
