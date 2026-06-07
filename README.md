# MathPlus

A lightweight, low-level Linear Algebra and Matrix manipulation library for Python. Developed from scratch, this module provides essential tools for multi-dimensional array transformations, vector spaces, and computer graphics math extensions without relying on heavy external dependencies.

---

## 🛠️ Features & Operations

*   **Matrix Arithmetic:** Support for core operations including Matrix Addition, Subtraction, and Scalar Multiplication.
*   **Matrix Multiplication:** Optimized native algorithms for Matrix-by-Matrix and Matrix-by-Vector transformations.
*   **Structural Transformations:** Fast execution for Matrix Transposition, Determinant calculations, and Inverse Matrix generation.
*   **Computer Graphics Ready:** Perfectly suited for constructing custom 2D/3D transformation matrices (Rotation, Scaling, and Translation pipelines).

---

## 📦 Tech Stack & Performance

*   **Language:** Python 3.14+
*   **Architecture:** Pure Python execution loops tailored for algorithmic transparency.
*   **Dependencies:** Zero external dependencies (Completely standalone).

---

## 🚀 Installation & Integration

You can easily drop `mathplus.py` into any custom 3D engine, physics simulator, or data science script.

### 1. Clone the repository
```bash
git clone https://github.com
cd module-lib
```

### 2. Integration Example
Simply move the `mathplus.py` file into your project workspace and import the matrix utility:

```python
import mathplus

# Create custom matrix structures (List of Lists representation)
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

# Perform linear algebra operations
result = mathplus.matrix_multiply(matrix_A, matrix_B)
print(f"Multiplied Matrix: {result}")
```

---

## 📐 Architecture & Usage Showcase

Here is a quick look at how the module handles internal matrix calculations seamlessly:

```python
from mathplus import transpose, determinant

matrix = [
    [1, 0, 2],
    [-1, 3, 0],
    [2, 1, 4]
]

# Calculate the matrix determinant
det = determinant(matrix)
print(f"Matrix Determinant: {det}")

# Transpose rows into columns
transposed_matrix = transpose(matrix)
print(f"Transposed Result: {transposed_matrix}")
```

---

## 📁 Repository Structure

```text
module-lib/
│
├── mathplus.py       # Linear algebra and core matrix operations
├── .gitattributes    # Git repository settings
└── README.md         # Documentation and architectural guide
```
