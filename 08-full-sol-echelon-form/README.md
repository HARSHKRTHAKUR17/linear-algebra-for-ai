# Lecture 08 - Complete Solution & Rank Cases

This lecture extends the concepts of Gaussian Elimination and RREF to completely classify the solutions of a linear system. It also introduces different rank conditions and their implications on the existence and uniqueness of solutions.

---

## Topics Covered

- Complete Solution of a Linear System
- Particular Solution
- Homogeneous Solution
- General Solution
- Full Column Rank
- Full Row Rank
- Full Rank
- Rank Deficient Matrices

---

## Mathematical Concepts

### Complete Solution

The complete solution of a linear system is given by

\[
x = x_p + x_n
\]

where:

- \(x_p\) = Particular Solution (satisfies \(Ax=b\))
- \(x_n\) = Null Space Solution (satisfies \(Ax=0\))

Thus, every solution of \(Ax=b\) can be expressed as the sum of one particular solution and one homogeneous solution.

---

### Rank Cases

#### 1. Full Column Rank

- Pivot in every column
- No free variables
- Unique solution (if the system is consistent)

---

#### 2. Full Row Rank

- Pivot in every row
- Solution exists for every right-hand side \(b\)
- May contain free variables
- Usually infinitely many solutions

---

#### 3. Full Rank

A matrix is said to be full rank if

rank(A) = min(number of rows, number of columns)

Examples

| Matrix Size | Rank | Classification |
|------------|------|----------------|
| 5 × 3 | 3 | Full Column Rank |
| 3 × 5 | 3 | Full Row Rank |
| 4 × 4 | 4 | Full Rank |
| 4 × 4 | 2 | Rank Deficient |

---

## Source Files

```
src/
├── complete_solution.py
└── rank_cases.py
```

---

## Tests

```
tests/
├── test_complete_solution.py
└── test_rank_cases.py
```

---

## Demo

Run the demonstration:

```bash
python demo.py
```

The demo showcases:

- Computing the complete solution
- Identifying pivot and free variables
- Checking whether a system has:
  - No solution
  - A unique solution
  - Infinitely many solutions
- Classifying matrices based on rank

---

## AI / Machine Learning Applications

### Linear Regression

- Full column rank ensures model parameters are uniquely identifiable.
- Rank-deficient feature matrices lead to multiple parameter vectors producing the same predictions.

---

### Deep Learning

Modern neural networks are often overparameterized.

This results in many valid parameter vectors that achieve similar training loss, analogous to systems with free variables.

---

### Principal Component Analysis (PCA)

Low-rank data matrices contain redundant information.

PCA exploits this property to obtain lower-dimensional representations while preserving most of the variance.

---

### Recommendation Systems

Matrix factorization techniques assume the user-item interaction matrix is approximately low rank.

This enables efficient prediction of missing ratings.

---

## Software Engineering Concepts

- Reuse previously implemented algorithms instead of rewriting them.
- Separate computation from interpretation.
- Return structured metadata rather than only numerical results.
- Build modular, reusable components.

---

## Key Takeaways

- Complete Solution = Particular Solution + Null Space Solution
- Full Column Rank ⇒ No Free Variables
- Full Row Rank ⇒ Solution Exists for Every \(b\)
- Full Rank ⇒ Rank equals the minimum of rows and columns
- Rank Deficiency indicates redundant information

---

## Dependencies

This lecture reuses functionality from the shared `core/` package.

```
core/
├── matrix.py
├── utils.py
├── echelon.py
├── rref.py
├── rank.py
└── pivots.py
```

---

## Next Lecture

Lecture 09 introduces:

- Linear Independence
- Basis
- Dimension
- Coordinate Systems

These concepts build directly upon the ideas of rank and pivot columns introduced in this lecture.