import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

os.makedirs("outputs/regression", exist_ok=True)

df = pd.read_csv("data/processed/final_dataset.csv")

X = df.drop(columns=["Date", "RealPrice"])
y = df["RealPrice"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
r2  = model.score(X, y)
mse = mean_squared_error(y, y_pred)

print("\n=== LINEAR REGRESSION RESULTS ===")

print("\nModel Equation:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: {coef:.2f}")
print(f"  Intercept: {model.intercept_:.2f}")

print(f"\nData period: {df['Date'].iloc[0]}  →  {df['Date'].iloc[-1]}")

print("\nModel Performance:")
print(f"  R^2: {r2:.4f}")
print(f"  MSE: {mse:.2f}")

print("\nSample Predictions:")
results = pd.DataFrame({
    "Date":      df["Date"].values,
    "Actual":    y.values,
    "Predicted": y_pred.round(2)
})
print(results.head(10))

results.to_csv("outputs/regression/predictions.csv", index=False)

with open("outputs/regression/results.txt", "w") as f:
    f.write("LINEAR REGRESSION RESULTS\n\n")
    f.write(f"Data: {df['Date'].iloc[0]} to {df['Date'].iloc[-1]}\n\n")
    f.write("Coefficients:\n")
    for name, coef in zip(X.columns, model.coef_):
        f.write(f"{name}: {coef:.2f}\n")
    f.write(f"\nIntercept: {model.intercept_:.2f}\n")
    f.write(f"R^2: {r2:.4f}\n")
    f.write(f"MSE: {mse:.2f}\n")

print("\nSaved outputs to /outputs folder")
