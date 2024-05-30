# VolumeCalculator

A simple library to calculate volumes of various geometric shapes.

## Installation

To install the VolumeCalculator library, use pip:

```sh
pip install git+https://github.com/antigenius0910/volume_calculator.git
```

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

### Script Usage
You can also use the included script volume_calculator_script.py to interactively calculate the volumes of different shapes. Run the script as follows:
```sh
python -m volume_calculator.volume_calculator_script
```

### Running the Flask App
```sh
export FLASK_APP=volume_calculator/app.py
flask run --host=0.0.0.0 --port=5050
```

### Running the Flask App in Docker
```sh
docker build -t volume_calculator_api .
docker run -p 5050:5050 volume_calculator_api
```

for Cube
```sh
curl -X POST -H "Content-Type: application/json" -d '{"shape": "cube", "dimensions": {"side_length": 3}}' http://127.0.0.1:5050/calculate_volume
```

for Cylinder
```sh
curl -X POST -H "Content-Type: application/json" -d '{"shape": "cylinder", "dimensions": {"radius": 3, "height": 5}}' http://127.0.0.1:5050/calculate_volume
```


### Running Tests

To run the tests, use [pytest](https://pytest.org/):
```sh
pytest tests/test_volume_calculator.py
```


### Additional Notes:

- Ensure that the `volume_calculator.py` file is in the same directory as `test_volume_calculator.py`.
- The `README.md` file should provides comprehensive information on the library, including installation instructions, usage examples, API documentation, testing instructions, and contribution guidelines. This will help users understand and utilize the library effectively.
