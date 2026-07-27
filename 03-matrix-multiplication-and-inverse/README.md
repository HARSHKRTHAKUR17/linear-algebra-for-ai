# Lecture 3 - Matrix Multiplication

## Overview

This module implements **Matrix Multiplication**, one of the most important operations in Linear Algebra.

Matrix multiplication represents the composition of linear transformations and forms the computational backbone of modern Artificial Intelligence, Machine Learning, Computer Vision, and Deep Learning.

---

# Topics Covered

- Matrix Multiplication
- Matrix Dimensions
- Dot Product
- Identity Matrix
- Matrix Inverse (Introduction)

---

# Project Structure

```text
03-matrix-multiplication/
│
├── core/
│   ├── matrix_multiplication.py
│   └── matrix_inverse.py
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

## `matrix_multiplication.py`

Implements matrix multiplication.

Features:

- Matrix × Matrix multiplication
- Matrix × Vector multiplication
- Dimension validation

---

## `matrix_inverse.py`

Introduces matrix inversion.

Features:

- Matrix inverse computation
- Invertibility checking

---

## `demo.py`

Demonstrates:

- Matrix multiplication
- Identity matrix
- Matrix inverse
- Matrix-vector multiplication

Run using

```bash
python examples/demo.py
```

---

# Mathematical Concepts

## Matrix Multiplication

Matrix multiplication combines two linear transformations into one.

If

```
A : X → Y

B : Y → Z
```

then

```
BA
```

represents the combined transformation.

---

## Identity Matrix

The identity matrix leaves every vector unchanged.

```
AI = IA = A
```

---

## Matrix Inverse

A matrix inverse "undoes" a linear transformation.

If

```
AA⁻¹ = I
```

then

```
A⁻¹
```

is the inverse of

```
A
```

---

# Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Matrix Multiplication | O(n³) |
| Matrix-Vector Multiplication | O(n²) |
| Matrix Inverse | O(n³) |

---

# AI & Machine Learning Applications

Matrix multiplication is everywhere in AI.

Applications include:

- Neural Networks
- Transformers
- Computer Vision
- Recommendation Systems
- Reinforcement Learning
- Graphics Processing
- Scientific Computing

Every neural network layer performs a matrix multiplication before applying an activation function.

---

# Key Takeaways

After completing this module, you should understand:

- Matrix multiplication
- Dimension compatibility
- Identity matrices
- Matrix inverses
- Matrix multiplication as composition of linear transformations

---

# References

- MIT 18.06 Linear Algebra — Gilbert Strang
- *Introduction to Linear Algebra* — Gilbert Strang
- NumPy Documentation

---

# Next Lecture

**Lecture 4 – LU Factorization**