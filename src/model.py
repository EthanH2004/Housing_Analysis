import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

os.makedirs("outputs/regression", exist_ok=True)

df = pd.read_csv("data/processed/final_dataset.csv")

# features and target
X = df.drop(columns=["Date", "RealPrice"])
y = df["RealPrice"]

# chronological 80/20 split — keep time order so future data is always the test set
split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

# train only on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# evaluate on the test set (data the model has never seen)
y_pred = model.predict(X_test)
r2  = model.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)

print("\n=== LINEAR REGRESSION RESULTS ===")

print("\nModel Equation:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: {coef:.2f}")
print(f"  Intercept: {model.intercept_:.2f}")

print(f"\nTrain period: {df['Date'].iloc[0]}  →  {df['Date'].iloc[split-1]}")
print(f"Test period:  {df['Date'].iloc[split]}  →  {df['Date'].iloc[-1]}")

print("\nModel Performance (test set):")
print(f"  R^2: {r2:.4f}")
print(f"  MSE: {mse:.2f}")

print("\nSample Predictions (test set):")
results = pd.DataFrame({
    "Date":      df["Date"].iloc[split:].values,
    "Actual":    y_test.values,
    "Predicted": y_pred.round(2)
})
print(results.head(10))

results.to_csv("outputs/regression/predictions.csv", index=False)

with open("outputs/regression/results.txt", "w") as f:
    f.write("LINEAR REGRESSION RESULTS\n\n")
    f.write(f"Train: {df['Date'].iloc[0]} to {df['Date'].iloc[split-1]}\n")
    f.write(f"Test:  {df['Date'].iloc[split]} to {df['Date'].iloc[-1]}\n\n")
    f.write("Coefficients:\n")
    for name, coef in zip(X.columns, model.coef_):
        f.write(f"{name}: {coef:.2f}\n")
    f.write(f"\nIntercept: {model.intercept_:.2f}\n")
    f.write(f"R^2 (test): {r2:.4f}\n")
    f.write(f"MSE (test): {mse:.2f}\n")

print("\nSaved outputs to /outputs folder")
