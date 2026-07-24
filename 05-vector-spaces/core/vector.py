from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class Vector:
    """
    Immutable mathematical vector backed by a NumPy array.
    """

    values: np.ndarray

    def __post_init__(self) -> None:
        array = np.asarray(self.values, dtype=float).reshape(-1)
        object.__setattr__(self, "values", array)

    @property
    def dimension(self) -> int:
        return self.values.size

    def norm(self) -> float:
        return float(np.linalg.norm(self.values))

    def dot(self, other: "Vector") -> float:
        self._check_dimension(other)
        return float(np.dot(self.values, other.values))

    def normalized(self) -> "Vector":
        n = self.norm()
        if np.isclose(n, 0):
            raise ValueError("Cannot normalize the zero vector.")
        return Vector(self.values / n)

    def distance_to(self, other: "Vector") -> float:
        self._check_dimension(other)
        return float(np.linalg.norm(self.values - other.values))

    def angle_with(self, other: "Vector") -> float:
        self._check_dimension(other)

        denominator = self.norm() * other.norm()

        if np.isclose(denominator, 0):
            raise ValueError("Angle with zero vector is undefined.")

        cosine = self.dot(other) / denominator
        cosine = np.clip(cosine, -1.0, 1.0)

        return float(np.degrees(np.arccos(cosine)))

    def is_zero(self) -> bool:
        return np.allclose(self.values, 0)

    def to_numpy(self) -> np.ndarray:
        return self.values.copy()

    def _check_dimension(self, other: "Vector") -> None:
        if self.dimension != other.dimension:
            raise ValueError(
                f"Dimension mismatch: {self.dimension} != {other.dimension}"
            )

    def __add__(self, other: "Vector") -> "Vector":
        self._check_dimension(other)
        return Vector(self.values + other.values)

    def __sub__(self, other: "Vector") -> "Vector":
        self._check_dimension(other)
        return Vector(self.values - other.values)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.values * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> "Vector":
        if np.isclose(scalar, 0):
            raise ZeroDivisionError("Division by zero.")
        return Vector(self.values / scalar)

    def __len__(self) -> int:
        return self.dimension

    def __iter__(self):
        return iter(self.values)

    def __repr__(self) -> str:
        return f"Vector({self.values.tolist()})"


def zeros(dimension: int) -> Vector:
    return Vector(np.zeros(dimension))


def ones(dimension: int) -> Vector:
    return Vector(np.ones(dimension))


def standard_basis(dimension: int) -> list[Vector]:
    basis = []

    for i in range(dimension):
        e = np.zeros(dimension)
        e[i] = 1
        basis.append(Vector(e))

    return basis


def from_list(values: Iterable[float]) -> Vector:
    return Vector(np.array(list(values), dtype=float))