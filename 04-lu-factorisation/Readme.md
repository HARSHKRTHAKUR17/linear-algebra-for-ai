# Lecture 4 - LU Factorization

## Overview

This module implements **LU Factorization**, one of the most important algorithms in Linear Algebra.

Instead of repeatedly performing Gaussian Elimination for every new system of equations, LU Factorization decomposes a matrix into two simpler matrices that can be reused to efficiently solve multiple systems.

If

```
Ax = b
```

then LU Factorization rewrites the system as

```
A = LU
```

where

- **L** is a Lower Triangular Matrix
- **U** is an Upper Triangular Matrix

The system becomes

```
LUx = b
```

which is solved in two simple steps:

```
Ly = b
Ux = y
```

This idea is widely used in scientific computing, numerical optimization, computer graphics, robotics, and machine learning.

---

# Topics Covered

- Gaussian Elimination
- LU Decomposition
- Lower Triangular Matrix
- Upper Triangular Matrix
- Forward Substitution
- Backward Substitution
- Solving Multiple Linear Systems

---

# Project Structure

```text
04-lu-factorization/
│
├── core/
│   ├── lu_decomposition.py
│   ├── forward_substitution.py
│   ├── backward_substitution.py
│   └── lu_solver.py
│
│
├── tests/
│
└── README.md
```

---

# File Descriptions

## `lu_decomposition.py`

Performs LU decomposition using Gaussian Elimination.

Features:

- Matrix decomposition
- Stores elimination multipliers
- Produces L and U matrices

---

## `forward_substitution.py`

Solves

```
Ly = b
```

where **L** is a lower triangular matrix.

Features:

- Forward substitution
- Intermediate solution vector

---

## `backward_substitution.py`

Solves

```
Ux = y
```

where **U** is an upper triangular matrix.

Features:

- Backward substitution
- Final solution vector

---

## `lu_solver.py`

Combines every step into a complete LU solver.

Pipeline:

```
A
│
├── LU Decomposition
│
├── Forward Substitution
│
├── Backward Substitution
│
└── Solution x
```

---

## `demo.py`

Demonstrates:

- LU decomposition
- Forward substitution
- Backward substitution
- Complete system solving

Run using

```bash
python examples/demo.py
```

---

# Mathematical Concepts

## Gaussian Elimination

Gaussian Elimination transforms a matrix into an upper triangular form by eliminating entries below the pivot.

Example:

```
2 1
4 3
```

↓

```
2 1
0 1
```

---

## LU Decomposition

Instead of discarding the elimination multipliers, LU decomposition stores them inside a lower triangular matrix.

```
A = LU
```

where

```
L =
1 0
2 1
```

and

```
U =
2 1
0 1
```

---

## Lower Triangular Matrix

A matrix whose entries above the diagonal are zero.

Example

```
1 0 0
2 1 0
5 4 1
```

---

## Upper Triangular Matrix

A matrix whose entries below the diagonal are zero.

Example

```
3 2 1
0 5 7
0 0 9
```

---

## Forward Substitution

After decomposition,

```
Ly = b
```

is solved by computing one variable at a time from top to bottom.

---

## Backward Substitution

Once

```
y
```

is known,

```
Ux = y
```

is solved from bottom to top.

---

# Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Gaussian Elimination | O(n³) |
| LU Decomposition | O(n³) |
| Forward Substitution | O(n²) |
| Backward Substitution | O(n²) |
| Solving Additional Systems | O(n²) |

---

# Why LU Factorization?

Suppose we need to solve

```
Ax = b₁
Ax = b₂
Ax = b₃
...
Ax = b₁₀₀
```

Without LU:

```
Gaussian Elimination
100 times
```

Cost:

```
100 × O(n³)
```

With LU:

```
One LU Decomposition

↓

100 Forward Substitutions

↓

100 Backward Substitutions
```

Cost:

```
O(n³) + 100 × O(n²)
```

This is significantly faster when the matrix remains unchanged.

---

# AI & Machine Learning Applications

LU decomposition is heavily used in numerical linear algebra libraries such as NumPy, SciPy, Eigen, LAPACK, and TensorFlow.

Applications include:

## Linear Regression

Many optimization algorithms repeatedly solve systems of linear equations.

---

## Newton's Method

Optimization algorithms require solving

```
Hx = b
```

where

```
H
```

is the Hessian matrix.

LU decomposition accelerates these computations.

---

## Robotics

Robot motion planning involves solving large systems of equations repeatedly.

---

## Physics Simulations

Finite Element Analysis and fluid simulations rely heavily on LU decomposition.

---

## Computer Graphics

Lighting, transformations, and physical simulations frequently solve linear systems.

---

## Scientific Computing

Engineering simulations often solve millions of linear systems using LU decomposition.

---

# Key Takeaways

After completing this module, you should understand:

- Why LU decomposition exists
- How Gaussian Elimination produces L and U
- The difference between lower and upper triangular matrices
- How forward substitution works
- How backward substitution works
- Why LU decomposition is efficient for solving multiple systems
- Where LU decomposition is used in scientific computing and AI

---

# References

- MIT 18.06 Linear Algebra — Gilbert Strang
- *Introduction to Linear Algebra* — Gilbert Strang
- NumPy Documentation
- LAPACK Documentation

---

# Next Lecture

**Lecture 5 – Vector Spaces**

Topics include:

- Vector Spaces
- Subspaces
- Linear Combinations
- Span
- Column Space
- Symmetric Matrices

These concepts form the mathematical foundation of modern Machine Learning, Deep Learning, and Artificial Intelligence.