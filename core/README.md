# Core Library

The `core/` directory contains reusable algorithms and utilities that are shared across multiple lectures of the MIT 18.06 Linear Algebra course.

Unlike the lecture folders, which contain concepts introduced in a particular lecture, the `core/` folder contains generic building blocks that can be reused throughout the project.

---

# Philosophy

The project follows a modular architecture.

```
Lecture
    │
    ▼
Uses reusable algorithms
    │
    ▼
core/
```

This prevents code duplication and makes the library easier to maintain and extend.

---

# Current Modules

## matrix.py

Provides common matrix operations and helper methods.

Examples include:

- Matrix creation
- Matrix validation
- Matrix dimensions
- Matrix printing
- Basic utility operations

---

## utils.py

Contains utility functions used throughout the project.

Examples include:

- Input validation
- Floating point comparisons
- Formatting functions
- Helper utilities

---

## echelon.py

Computes the Row Echelon Form (REF) of a matrix using Gaussian Elimination.

Used by:

- Rank
- RREF
- Linear System Solving
- Future decomposition algorithms

---

## rref.py

Computes the Reduced Row Echelon Form (RREF).

Used by:

- Complete Solution
- Null Space
- Column Space
- Matrix Inverse
- Future lectures

---

## pivots.py

Provides helper functions for identifying:

- Pivot Columns
- Pivot Rows
- Free Columns

Used by:

- Rank
- Basis
- Linear Independence
- Null Space
- Complete Solution

---

## rank.py

Computes the rank of a matrix.

Used by:

- Rank Classification
- Full Rank Checks
- Basis
- Dimension
- Least Squares
- Future AI/ML algorithms

---

# Design Principles

The `core/` library follows several software engineering principles.

## Single Responsibility Principle

Each module performs one well-defined task.

Example:

- `rank.py` computes rank.
- `rref.py` computes RREF.
- `pivots.py` identifies pivots.

---

## Reusability

Algorithms are implemented once and reused everywhere.

For example,

```
Gaussian Elimination
        │
        ├── Rank
        ├── RREF
        ├── Complete Solution
        ├── Basis
        └── Least Squares
```

---

## Modularity

Each lecture builds upon previous work instead of rewriting algorithms.

---

## Maintainability

Bug fixes or optimizations in one module automatically improve every lecture that depends on it.

---

# Folder Structure

```
core/
│
├── README.md
├── __init__.py
├── matrix.py
├── utils.py
├── echelon.py
├── rref.py
├── pivots.py
├── rank.py
└── ...
```

The folder will continue to grow as more reusable algorithms are introduced throughout the course.

---

# Future Modules

As the MIT 18.06 course progresses, additional reusable modules will be added here.

Planned modules include:

- null_space.py
- column_space.py
- basis.py
- independence.py
- projection.py
- orthogonality.py
- least_squares.py
- determinant.py
- eigenvalues.py
- eigenvectors.py
- qr.py
- svd.py

---

# Usage

Example:

```python
from core.rank import rank
from core.rref import rref
from core.echelon import echelon_form

A = [
    [1, 2],
    [3, 4]
]

print(rank(A))
```

Lecture-specific code imports these reusable modules instead of implementing the algorithms again.

---

# Goal

The objective of the `core/` package is to evolve into a complete, reusable Linear Algebra library built from first principles while studying MIT 18.06.

By the end of the course, this library will contain implementations of the fundamental algorithms used in mathematics, machine learning, computer graphics, optimization, and modern artificial intelligence.