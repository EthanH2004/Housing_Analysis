import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# load data
df = pd.read_csv("data/processed/final_dataset.csv")

# features + target
X = df[["InterestRate", "UnemploymentRate"]]
y = df["RealPrice"]

# train model
model = LinearRegression()
model.fit(X, y)

# predictions
y_pred = model.predict(X)

# metrics
r2 = model.score(X, y)
mse = mean_squared_error(y, y_pred)

# ===== CLEAN PRINTS =====
print("\n=== LINEAR REGRESSION RESULTS ===")

print("\nModel Equation:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: {coef:.2f}")
print(f"  Intercept: {model.intercept_:.2f}")

print("\nModel Performance:")
print(f"  R^2: {r2:.4f}")
print(f"  MSE: {mse:.2f}")

print("\nSample Predictions:")
results = pd.DataFrame({
    "Actual": y,
    "Predicted": y_pred.round(2)
})
print(results.head(10))

# ===== SAVE OUTPUTS =====

# save predictions
results.to_csv("outputs/predictions.csv", index=False)

# save summary text
with open("outputs/results.txt", "w") as f:
    f.write("LINEAR REGRESSION RESULTS\n\n")
    
    f.write("Coefficients:\n")
    for name, coef in zip(X.columns, model.coef_):
        f.write(f"{name}: {coef:.2f}\n")
    
    f.write(f"\nIntercept: {model.intercept_:.2f}\n")
    f.write(f"R^2: {r2:.4f}\n")
    f.write(f"MSE: {mse:.2f}\n")

print("\nSaved outputs to /outputs folder")