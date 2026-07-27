# Lecture 1 - Gaussian Elimination

## Overview

This module implements **Gaussian Elimination**, one of the most fundamental algorithms in Linear Algebra.

Gaussian Elimination transforms a system of linear equations into an equivalent upper triangular system, making it much easier to solve.

This algorithm is the foundation of many numerical methods used in engineering, scientific computing, artificial intelligence, and optimization.

---

# Topics Covered

- Systems of Linear Equations
- Matrix Representation
- Elementary Row Operations
- Pivot Elements
- Row Echelon Form
- Gaussian Elimination

---

# Project Structure

```text
01-gaussian-elimination/
│
├── core/
│   └── gaussian_elimination.py
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

## `gaussian_elimination.py`

Implements Gaussian Elimination using elementary row operations.

Features:

- Partial pivoting
- Row swapping
- Forward elimination
- Upper triangular matrix generation

---

## `demo.py`

Demonstrates Gaussian Elimination on sample systems.

Run using

```bash
python examples/demo.py
```

---

# Mathematical Concepts

## System of Linear Equations

Example

```
2x + y = 5
x + 3y = 7
```

can be represented as

```
Ax = b
```

---

## Elementary Row Operations

- Swap two rows
- Multiply a row by a non-zero scalar
- Add a multiple of one row to another

These operations preserve the solution.

---

## Pivot

A pivot is the leading non-zero element used to eliminate entries below it.

---

## Row Echelon Form

After elimination, the matrix becomes upper triangular, allowing efficient solution by backward substitution.

---

# Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Gaussian Elimination | O(n³) |

---

# AI & Machine Learning Applications

Gaussian Elimination is used in:

- Solving linear systems
- Scientific computing
- Numerical optimization
- Physics simulations
- Computer graphics
- Engineering software

---

# Key Takeaways

After completing this module, you should understand:

- Matrix representation of linear systems
- Elementary row operations
- Pivot selection
- Gaussian Elimination
- Row Echelon Form

---

# References

- MIT 18.06 Linear Algebra — Gilbert Strang
- *Introduction to Linear Algebra* — Gilbert Strang
- NumPy Documentation

---

# Next Lecture

**Lecture 2 – Backward Substitution**