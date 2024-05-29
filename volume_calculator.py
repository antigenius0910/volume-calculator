import math

class VolumeCalculator:
    @staticmethod
    def cube(side_length: float) -> float:
        """Calculate the volume of a cube."""
        if side_length <= 0:
            raise ValueError("Side length must be greater than zero")
        return side_length ** 3

    @staticmethod
    def sphere(radius: float) -> float:
        """Calculate the volume of a sphere."""
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        return (4/3) * math.pi * radius ** 3

    @staticmethod
    def cylinder(radius: float, height: float) -> float:
        """Calculate the volume of a cylinder."""
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be greater than zero")
        return math.pi * radius ** 2 * height

    @staticmethod
    def cone(radius: float, height: float) -> float:
        """Calculate the volume of a cone."""
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be greater than zero")
        return (1/3) * math.pi * radius ** 2 * height

# Example usage
if __name__ == "__main__":
    try:
        print("Volume of cube:", VolumeCalculator.cube(3))
        print("Volume of sphere:", VolumeCalculator.sphere(4))
        print("Volume of cylinder:", VolumeCalculator.cylinder(5, 7))
        print("Volume of cone:", VolumeCalculator.cone(6, 8))
    except ValueError as e:
        print("Error:", e)

