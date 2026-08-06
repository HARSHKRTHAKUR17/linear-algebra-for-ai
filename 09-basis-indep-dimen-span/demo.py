from core.independence import (
    is_independent,
    is_dependent,
)

from core.span import (
    spans_space,
    span_dimension,
)

from core.basis import is_basis

from core.dimension import dimension


vectors = [
    [1, 0],
    [0, 1]
]

print("Vectors")
print(vectors)

print()

print("Independent:", is_independent(vectors))
print("Dependent:", is_dependent(vectors))

print()

print("Spans R^n:", spans_space(vectors))
print("Span Dimension:", span_dimension(vectors))

print()

print("Is Basis:", is_basis(vectors))

print()

print("Dimension:", dimension(vectors))