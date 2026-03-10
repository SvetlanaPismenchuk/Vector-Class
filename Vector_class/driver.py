from vector import Vector

# Display the documentation for the Vector class
help(Vector)

# Create vector u directly with all three components
u = Vector(2, -2, 1)

# Create vector v as the zero vector, then set y and z manually
v = Vector()
v.y = 2
v.z = 1

# Print both vectors
print("u =", u)
print("v =", v)

# Test the dot product in both orders
print("u dot v =", u.dot(v))
print("v dot u =", v.dot(u))

# Compute and print the angle between the vectors
print("angle between u and v =", u.angle(v))

# Print norm of u before normalization
print("norm of u before normalization =", u.norm())

# Normalize u and print the updated vector
u.normalize()
print("u after normalization =", u)

# Print norm of u again to confirm it is a unit vector
print("norm of u after normalization =", u.norm())