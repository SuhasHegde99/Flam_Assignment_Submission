import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution, least_squares

# Load data
df = pd.read_csv("xy_data.csv")
x_data = df.iloc[:,0].values
y_data = df.iloc[:,1].values

# Generate t values
t = np.linspace(6, 60, len(df))

# Parametric model
def model_xy(params, t_vals):
    theta, M, X = params
    exp_term = np.exp(M * np.abs(t_vals))
    x = t_vals*np.cos(theta) - exp_term*np.sin(0.3*t_vals)*np.sin(theta) + X
    y = 42 + t_vals*np.sin(theta) + exp_term*np.sin(0.3*t_vals)*np.cos(theta)
    return x, y

# L1 loss
def l1_loss(params):
    x_pred, y_pred = model_xy(params, t)
    return np.sum(np.abs(x_pred - x_data) + np.abs(y_pred - y_data))

# Parameter bounds
bounds = [(0, np.deg2rad(50)), (-0.05, 0.05), (0, 100)]

# Differential Evolution
result = differential_evolution(lambda p: l1_loss(p), bounds, maxiter=400, polish=True)

# Least Squares refinement
def residuals(params):
    x_pred, y_pred = model_xy(params, t)
    return np.concatenate([x_pred - x_data, y_pred - y_data])

res = least_squares(residuals, result.x)

theta, M, X = res.x

# Print results
print("Theta (rad):", theta)
print("Theta (deg):", np.rad2deg(theta))
print("M:", M)
print("X:", X)

# Plot
x_fit, y_fit = model_xy(res.x, t)
plt.figure(figsize=(8,6))
plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_fit, y_fit, '-', label='Fitted Curve')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Data vs Fitted Parametric Curve")
plt.grid(True)
plt.savefig("fit_plot.png")
plt.show()

# Save results
with open("fit_results.txt", "w") as f:
    f.write(f"theta_rad={theta}\n")
    f.write(f"theta_deg={np.rad2deg(theta)}\n")
    f.write(f"M={M}\n")
    f.write(f"X={X}\n")
