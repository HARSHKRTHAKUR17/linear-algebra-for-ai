# Lecture 2 - Backward Substitution

## Overview

This module implements **Backward Substitution**, the algorithm used to solve an upper triangular system produced by Gaussian Elimination.

Once the matrix has been transformed into row echelon form, the unknown variables can be computed efficiently starting from the last equation and working upward.

---

# Topics Covered

- Upper Triangular Matrices
- Backward Substitution
- Solving Linear Systems

---

# Project Structure

```text
02-back-substitution/
│
├── core/
│   └── backward_substitution.py
│
├── examples/
│   └── demo.py
│
├── tests/
│
└── README.md
```

---

# File Descriptions

## `backward_substitution.py`

Solves an upper triangular system.

Features:

- Efficient triangular solving
- Numerical stability
- Reusable implementation

---

## `demo.py`

Demonstrates solving systems after Gaussian Elimination.

Run using

```bash
python examples/demo.py
```

---

# Mathematical Concepts

## Upper Triangular Matrix

Example

```
2 1 3
0 4 5
0 0 6
```

All entries below the diagonal are zero.

---

## Backward Substitution

Starting from the last equation:

```
6z = 18
```

↓

```
z = 3
```

Substitute into previous equations until every variable is found.

---

# Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Backward Substitution | O(n²) |

---

# AI & Machine Learning Applications

Backward substitution appears whenever triangular systems arise, including:

- LU decomposition
- QR decomposition
- Scientific computing
- Numerical optimization
- Machine learning libraries

---

# Key Takeaways

After completing this module, you should understand:

- Upper triangular matrices
- Backward substitution
- Efficient solving of linear systems

---

# References

- MIT 18.06 Linear Algebra — Gilbert Strang
- *Introduction to Linear Algebra* — Gilbert Strang

---

# Next Lecture

**Lecture 3 – Matrix Multiplication**