# Flam Research – Parametric Curve Fitting Assignment

## 🔍 Objective

Estimate the unknown parameters **θ**, **M**, and **X** in the given parametric equations so that the resulting curve best fits the provided `(x, y)` dataset.  
The curve equations:

\[
x(t) = t\cos\theta - e^{M|t|}\sin(0.3t)\sin\theta + X
\]

\[
y(t) = 42 + t\sin\theta + e^{M|t|}\sin(0.3t)\cos\theta
\]

---

## ✅ Final Estimated Parameters (Unknown Variables)

- **θ (theta)** = **0.516313 rad** (≈ 29.5826°)
- **M** = **−0.050000**
- **X** = **55.013536**

---

## 🎯 Final Required Submission (LaTeX Parametric Form)

\left(t*\cos(0.516313)-e^{-0.05\left|t\right|}\cdot\sin(0.3t)\sin(0.516313)+55.013536,42+t*\sin(0.516313)+e^{-0.05\left|t\right|}\cdot\sin(0.3t)\cos(0.516313)\right)

---

## 🧠 Methodology & Thought Process

### 1. Understanding the Problem
We must fit a nonlinear parametric curve to spatial data.

### 2. Preparing the Data
- Loaded `xy_data.csv`
- Sampled `t` uniformly from **6 to 60**

### 3. Model Implementation
Implemented the given parametric equations in Python.

### 4. Optimization Strategy

#### Global search (Differential Evolution)
- Robust for non-convex problems  
- L1 loss minimized  

#### Local refinement (Least Squares)
- Further improved solution accuracy

### 5. Final Result
The parameters listed above represent the best fit.

---

## 📁 Repository Contents

- `README.md`
- `main.py`
- `xy_data.csv`
- `fit_results.txt`
- `fit_plot.png`

---

## ▶️ How to Run

```
pip install numpy pandas scipy matplotlib
python main.py
```

---

## 🏁 Final Answer

\left(t*\cos(0.516313)-e^{-0.05\left|t\right|}\cdot\sin(0.3t)\sin(0.516313)+55.013536,42+t*\sin(0.516313)+e^{-0.05\left|t\right|}\cdot\sin(0.3t)\cos(0.516313)\right)