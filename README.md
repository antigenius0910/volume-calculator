# VolumeCalculator

A simple library to calculate volumes of various geometric shapes.


## Usage
```python
from volume_calculator import VolumeCalculator

# Calculate the volume of a cube
cube_volume = VolumeCalculator.cube(3)
print(f"Volume of cube: {cube_volume}")

# Calculate the volume of a sphere
sphere_volume = VolumeCalculator.sphere(4)
print(f"Volume of sphere: {sphere_volume}")

# Calculate the volume of a cylinder
cylinder_volume = VolumeCalculator.cylinder(3, 5)
print(f"Volume of cylinder: {cylinder_volume}")

# Calculate the volume of a cone
cone_volume = VolumeCalculator.cone(3, 5)
print(f"Volume of cone: {cone_volume}")
```


### Running Tests

To run the tests, use [pytest](https://pytest.org/):

```sh
pytest test_volume_calculator.py
```


### Additional Notes:

- Ensure that the `volume_calculator.py` file is in the same directory as `test_volume_calculator.py`.
- The `README.md` file should provides comprehensive information on the library, including installation instructions, usage examples, API documentation, testing instructions, and contribution guidelines. This will help users understand and utilize the library effectively.
