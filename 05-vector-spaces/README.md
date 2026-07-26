# Lecture 5 - Vector Spaces

## Overview

This module implements the fundamental concepts introduced in **MIT 18.06 Linear Algebra – Lecture 5: Vector Spaces**.

Unlike the previous lectures, which focused on algorithms for solving systems of linear equations, this lecture introduces the idea of viewing vectors as elements of mathematical spaces. These concepts form the mathematical foundation of modern Machine Learning, Deep Learning, Computer Vision, Natural Language Processing, and Scientific Computing.

---

## Topics Covered

- Vector Spaces
- Subspaces
- Linear Combinations
- Span
- Column Space
- Symmetric Matrices

---

## Project Structure

```text
05-vector-spaces/
│
├── core/
│   ├── vector.py
│   ├── linear_combination.py
│   ├── subspace.py
│   ├── column_space.py
│   └── symmetric_matrix.py
│
├── examples/
│   └── examples.py
│
├── tests/
│
└── README.md
```

---

## File Descriptions

### `vector.py`

Implements a reusable mathematical vector class.

Features:

- Vector addition
- Vector subtraction
- Scalar multiplication
- Scalar division
- Dot product
- Euclidean norm
- Zero vector detection

---

### `linear_combination.py`

Implements operations involving linear combinations.

Features:

- Compute linear combinations
- Build coefficient matrices
- Determine whether a vector belongs to a span
- Solve for unknown coefficients

---

### `subspace.py`

Implements operations related to subspaces.

Features:

- Subspace dimension
- Membership testing
- Span verification

---

### `column_space.py`

Implements utilities for working with the column space of a matrix.

Features:

- Extract column vectors
- Compute column rank
- Display column space

---

### `symmetric_matrix.py`

Implements basic symmetric matrix operations.

Features:

- Matrix transpose
- Symmetric matrix detection
- Matrix information display

---

### `examples.py`

Contains demonstrations of every concept implemented in this module.

Run:

```bash
python examples/examples.py
```

---

## Mathematical Concepts

This lecture introduces several fundamental ideas:

### Vector Space

A collection of vectors that is closed under

- Vector addition
- Scalar multiplication

---

### Subspace

A subset of a vector space that is itself a vector space.

Examples include:

- Column Space
- Null Space (introduced later)
- Row Space (introduced later)

---

### Linear Combination

A vector formed by multiplying vectors by scalars and adding them together.

Example:

```text
2v₁ - 3v₂ + v₃
```

---

### Span

The set of **all possible linear combinations** of a collection of vectors.

The span tells us every vector that can be generated from those vectors.

---

### Column Space

The span of all columns of a matrix.

The column space represents every vector that can be produced by the matrix multiplication:

```text
Ax
```

---

### Symmetric Matrix

A matrix is symmetric if

```text
A = Aᵀ
```

Symmetric matrices appear frequently in optimization, statistics, covariance matrices, and machine learning.

---

## Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Vector Addition | O(n) |
| Dot Product | O(n) |
| Vector Norm | O(n) |
| Linear Combination | O(n × m) |
| Matrix Rank | O(min(m,n)³) |
| Symmetric Check | O(n²) |

---

## AI & Machine Learning Applications

The concepts introduced in this lecture appear throughout AI and Machine Learning.

### Feature Vectors

Every data sample can be represented as a vector.

Examples:

- House prices
- Images
- Audio
- Sensor data

---

### Word Embeddings

Models such as Word2Vec, GloVe, and modern LLMs represent words as vectors in high-dimensional vector spaces.

---

### Neural Networks

Every layer transforms one vector space into another.

```
Input Vector
      ↓
Linear Layer
      ↓
Hidden Vector
      ↓
Activation
      ↓
Output Vector
```

---

### Computer Vision

Images are represented as vectors before being processed by neural networks.

---

### Recommendation Systems

Users and items are represented in shared latent vector spaces.

---

### Transformers

Token embeddings, positional embeddings, attention vectors, and hidden states all live in vector spaces.

---

## Key Takeaways

After completing this module, you should understand:

- What a vector space is
- What makes a subset a subspace
- How linear combinations generate new vectors
- What the span of vectors represents
- The meaning of the column space
- How to identify symmetric matrices
- Why vector spaces are fundamental to modern AI

---

## References

- MIT 18.06 Linear Algebra — Gilbert Strang
- *Introduction to Linear Algebra* — Gilbert Strang
- NumPy Documentation
- SciPy Documentation

---

