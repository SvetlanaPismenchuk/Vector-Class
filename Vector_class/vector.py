import math

class Vector:
    """
    A class used to represent a 3D vector.

    Each vector has x, y, and z components, and the class provides
    methods for common vector operations such as finding the magnitude,
    normalizing the vector, computing the dot product, and finding
    the angle between two vectors.
    """

    def __init__(self, x=0, y=0, z=0):
        """
        Initialize a Vector object.

        Parameters:
            x (float): The x-component of the vector.
            y (float): The y-component of the vector.
            z (float): The z-component of the vector.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Return a string representation of the vector in angle bracket notation.

        Returns:
            str: The vector written as <x,y,z>.
        """
        return f"<{self.x},{self.y},{self.z}>"

    def norm(self):
        """
        Return the Euclidean norm (magnitude) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """
        Convert the vector into a unit vector by dividing each component
        by the vector's magnitude.

        This method modifies the vector directly and does not return anything.
        """
        magnitude = self.norm()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude
            self.z /= magnitude

    def dot(self, v):
        """
        Return the dot product of this vector and another vector.

        Parameters:
            v (Vector): Another Vector object.

        Returns:
            float: The dot product.
        """
        return self.x * v.x + self.y * v.y + self.z * v.z

    def angle(self, v):
        """
        Return the angle in radians between this vector and another vector.

        Parameters:
            v (Vector): Another Vector object.

        Returns:
            float: The angle in radians between the two vectors.
        """
        numerator = self.dot(v)
        denominator = self.norm() * v.norm()

        if denominator == 0:
            raise ValueError("Cannot calculate an angle with a zero vector.")

        value = numerator / denominator

        # Helps avoid small floating-point issues outside [-1, 1]
        value = max(-1, min(1, value))

        return math.acos(value)