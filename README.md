# 🛡️ LCG Predictor & Cryptanalysis Tool

This repository contains a Python-based exploit/tool designed to reverse engineer **Linear Congruential Generators (LCG)**. By observing a small window of output, this script can derive the internal constants and predict every future number in the sequence from a table.

---

## 📖 Theoretical Background

A Linear Congruential Generator (LCG) is a common algorithm for yielding a sequence of pseudo-randomized numbers. It is defined by the recurrence relation:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

Where:
* **$X$**: The sequence of pseudo-random values.
* **$m > 0$**: The "modulus".
* **$a$**: The "multiplier" ($0 < a < m$).
* **$c$**: The "increment" ($0 \le c < m$).

While fast, LCGs are **not cryptographically secure**. If the modulus ($m$) is known, we only need three consecutive values to completely break the generator.

---

## 🧠 How the Exploit Works

The tool performs a **Three-Point Attack**:

1.  **Calculate the Multiplier ($a$):**
    The difference between consecutive values follows the rule: 
    $(X_3 - X_2) \equiv a(X_2 - X_1) \pmod m$.
    We solve for $a$ by calculating the **Modular Multiplicative Inverse** of $(X_2 - X_1)$.

2.  **Calculate the Increment ($c$):**
    Once $a$ is known, $c$ is found via: 
    $c \equiv (X_2 - aX_1) \pmod m$.

3.  **Verification:**
    The script validates the constants against the third known value to ensure the prediction is 100% accurate.

---

## 🚀 Features

* **Interactive CLI:** Input values in real-time during CTFs.
* **High Precision:** Handles extremely large prime moduli (e.g., 64-bit integers).
* **No Dependencies:** Uses pure Python 3.8+ (`pow(a, -1, m)` logic).
* **Fast Prediction:** Instantaneously derives constants and predicts the next state.

---

## 🛠️ Usage

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-user/lcg-predictor.git](https://github.com/your-user/lcg-predictor.git)
   cd lcg-predictor
