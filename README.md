
# Parametric Curve Fitting – Flam Research Assignment

## Final Estimated Parameters
- **θ (theta)** = 0.516313 rad (≈ 29.5826°)
- **M** = -0.050000
- **X** = 55.013536

## Final Parametric Equations

```
x(t) = t*cos(0.516313) - e^(-0.05*|t|) * sin(0.3*t) * sin(0.516313) + 55.013536
y(t) = 42 + t*sin(0.516313) + e^(-0.05*|t|) * sin(0.3*t) * cos(0.516313)
```

These equations can be used directly in Desmos for verification.

---

## Approach Summary
1. Loaded the given `xy_data.csv`.
2. Assumed `t` ranges from 6 to 60 (uniform spacing).
3. Defined the parametric model.
4. Applied **Differential Evolution** for global optimization.
5. Refined results using **Least Squares**.
6. Extracted final parameters and plotted fitted curve.

---

## How to Run

Install dependencies:
```
pip install numpy pandas scipy matplotlib
```

Run the fitting script:
```
python main.py
```

Outputs will include:
- Final parameter values  
- Curve plot (`fit_plot.png`)  
- Results text file (`fit_results.txt`)  

---

## Files Included
- `main.py`
- `xy_data.csv`
- `fit_results.txt`
- `fit_plot.png`
- `README.md`

