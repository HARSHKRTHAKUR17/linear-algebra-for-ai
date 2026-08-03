# Linear Algebra from Scratch using MIT 18.06

A comprehensive Linear Algebra library and learning repository built while studying **MIT 18.06 - Linear Algebra by Prof. Gilbert Strang**.

This project combines mathematical theory, Python implementations, software engineering practices, testing, and AI/ML applications into a single structured repository.

The goal is not only to learn Linear Algebra, but also to build a reusable Python library that can later be used in Machine Learning, Deep Learning, Computer Vision, Natural Language Processing, Reinforcement Learning, Robotics, and Large Language Models.

---

# Objectives

- Learn Linear Algebra from first principles.
- Implement every important algorithm from scratch.
- Build a reusable Linear Algebra Python library.
- Understand where each concept is used in AI/ML.
- Practice clean software engineering.
- Create a production-quality GitHub portfolio project.

---

# Repository Structure

```
Linear-Algebra/
│
├── core/
│   ├── README.md
│   ├── matrix.py
│   ├── utils.py
│   ├── echelon.py
│   ├── rref.py
│   ├── pivots.py
│   ├── rank.py
│   └── ...
│
├── lecture01_linear_equations/
├── lecture02_elimination/
├── lecture03_matrix_multiplication/
├── lecture04_lu_factorization/
├── lecture05_vector_spaces/
├── lecture06_column_null_space/
├── lecture07_echelon_rank/
├── lecture08_complete_solution/
│
├── README.md
└── requirements.txt
```

---

# Project Architecture

The repository follows a modular architecture.

```
Lecture
      │
      ▼
Imports reusable algorithms
      │
      ▼
core/
```

The `core/` package contains reusable implementations shared across multiple lectures.

Each lecture folder contains:

- source code
- demonstrations
- tests
- lecture notes
- documentation

This separation prevents code duplication and mirrors how professional Python libraries are organized.

---

# Course Progress

| Lecture | Topic | Status |
|----------|--------|--------|
| 1 | Linear Equations | ✅ |
| 2 | Gaussian Elimination | ✅ |
| 3 | Matrix Multiplication & Inverse | ✅ |
| 4 | LU Factorization | ✅ |
| 5 | Vector Spaces | ✅ |
| 6 | Column Space & Null Space | ✅ |
| 7 | Echelon Form, Rank & RREF | ✅ |
| 8 | Complete Solution & Rank Cases | ✅ |

---

# Concepts Learned

## Lecture 1

- Systems of Linear Equations
- Matrix Representation
- Elimination

---

## Lecture 2

- Gaussian Elimination
- Pivoting
- Forward Elimination
- Back Substitution

---

## Lecture 3

- Matrix Multiplication
- Four Ways of Matrix Multiplication
- Identity Matrix
- Matrix Inverse
- Gauss-Jordan Elimination

---

## Lecture 4

- LU Factorization
- Lower Triangular Matrix
- Upper Triangular Matrix
- Forward Substitution
- Backward Substitution
- PA = LU

---

## Lecture 5

- Symmetric Matrices
- Vector Spaces
- Subspaces
- Column Space

---

## Lecture 6

- Null Space
- Column Space
- Vector Space Properties
- Solutions of Ax = 0
- Solutions of Ax = b

---

## Lecture 7

- Row Echelon Form
- Reduced Row Echelon Form
- Rank
- Pivot Columns
- Pivot Rows
- Free Variables
- General Solution

---

## Lecture 8

- Complete Solution
- Particular Solution
- Homogeneous Solution
- Full Column Rank
- Full Row Rank
- Full Rank
- Rank Deficient Matrices

---

# Current Core Library

Reusable implementations currently available:

- Matrix Utilities
- Gaussian Elimination
- Row Echelon Form
- Reduced Row Echelon Form
- Pivot Detection
- Rank Computation

The core library will continue to expand throughout the course.

---

# AI / Machine Learning Applications

This repository highlights how Linear Algebra is used in modern Artificial Intelligence.

Current applications covered include:

- Feature Engineering
- Feature Redundancy
- Linear Regression
- Principal Component Analysis (PCA)
- Matrix Factorization
- Neural Networks
- Overparameterized Models
- Recommendation Systems

Future lectures will include:

- Least Squares
- Eigenvalues
- Eigenvectors
- Singular Value Decomposition (SVD)
- Principal Component Analysis
- Gradient Descent
- Neural Network Mathematics
- Transformers
- Large Language Models

---

# Software Engineering Principles

This project follows modern software engineering practices.

- Modular Design
- Single Responsibility Principle
- Code Reusability
- Separation of Concerns
- Unit Testing
- Documentation
- Clean Project Structure

---

# Testing

Each lecture contains dedicated unit tests for newly implemented algorithms.

```
tests/
```

The project uses **pytest**.

Run all tests:

```bash
pytest
```

---

# Future Roadmap

Topics that will be implemented later include:

- Linear Independence
- Basis
- Dimension
- Orthogonality
- Orthogonal Projection
- Least Squares
- Determinants
- Eigenvalues
- Eigenvectors
- Positive Definite Matrices
- Singular Value Decomposition
- Principal Component Analysis
- Markov Matrices
- Fast Fourier Transform

---

# References

- MIT 18.06 – Linear Algebra
- Prof. Gilbert Strang
- Introduction to Linear Algebra (Gilbert Strang)

---

# Author

Developed while studying **MIT 18.06 – Linear Algebra** with the objective of building a complete Linear Algebra library from scratch and applying it to Artificial Intelligence and Machine Learning.