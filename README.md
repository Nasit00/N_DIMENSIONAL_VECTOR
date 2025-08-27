# N_DIMENSIONAL_VECTOR
n_dimensional_Vector

A Python class implementation of an n-dimensional vector with support for basic vector operations such as addition, dot product, cross product, and cloning.

This project demonstrates operator overloading, object-oriented programming, and mathematical abstractions in Python.

✨ Features

✅ Create vectors of any dimension

✅ Indexing and assignment (v[i])

✅ Equality check (==)

✅ String representation for readability

✅ Vector addition (+)

✅ Dot product (@)

✅ Cross product (for 3D vectors)

✅ Clone vectors (deep copy)

📂 Class Overview
Attributes

values: list of vector elements

size: number of dimensions

Methods

__init__(*n) → initialize vector with given values

__getitem__(index) → access element by index

__setitem__(index, value) → set element by index

__str__() → string representation

__eq__(other) → check vector equality

__add__(other) → vector addition

__matmul__(other) → dot product

cross_product(other) → cross product (only for 3D)

clone() → create a copy of the vector

📝 Example Usage
from n_dimensional_Vector import n_dimensional_Vector

# Create vectors
v1 = n_dimensional_Vector(1, 2, 3)
v2 = n_dimensional_Vector(4, 5, 6)

# String representation
print(v1)  
# Output: Vector [1, 2, 3] and size is 3

# Vector addition
print(v1 + v2)  
# Output: Vector [5, 7, 9] and size is 3

# Dot product
print(v1 @ v2)  
# Output: 32

# Cross product
print(v1.cross_product(v2))  
# Output: Vector [-3, 6, -3] and size is 3

# Clone vector
v3 = v1.clone()
print(v3)  
# Output: Vector [1, 2, 3] and size is 3

🚀 Future Improvements

Add scalar multiplication/division

Implement magnitude and normalization

Support advanced vector operations (angle, projection, etc.)
