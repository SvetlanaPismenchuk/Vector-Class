# Vector Class Project

## Overview

This repository contains a Python module named `vector.py` that defines a `Vector` class for working with 3D vectors. The class includes attributes for the x-, y-, and z-components and methods for common vector operations.

## Vector Class

The `Vector` class represents a vector in three-dimensional space.

### Attributes

- `x` : the x-component of the vector
- `y` : the y-component of the vector
- `z` : the z-component of the vector

### Methods

- `__init__(x=0, y=0, z=0)`
  - Creates a new vector with the given x, y, and z values.
  - All components default to 0.

- `__str__()`
  - Returns the vector as a string in angle bracket notation.
  - Example: `<2,-3,1>`

- `norm()`
  - Returns the Euclidean norm, or magnitude, of the vector.

- `normalize()`
  - Converts the vector into a unit vector by dividing each component by the magnitude.
  - This method changes the vector directly and does not return anything.

- `dot(v)`
  - Returns the dot product of this vector and another vector `v`.

- `angle(v)`
  - Returns the angle in radians between this vector and another vector `v`.

## How to Import the Class

```python
from vector import Vector
```


## Example
```python
from vector import Vector

v1 = Vector(3, 0, -4)
v2 = Vector(1, 2, 3)

print(v1)             # <3,0,-4>
print(v1.norm())      # 5.0
print(v1.dot(v2))     # -9

v1.normalize()
print(v1)             # <0.6,0.0,-0.8>

print(v1.angle(v2))   # angle in radians
```