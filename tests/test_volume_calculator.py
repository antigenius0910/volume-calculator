import pytest
from volume_calculator import VolumeCalculator

def test_cube():
    assert VolumeCalculator.cube(3) == 27
    assert VolumeCalculator.cube(0.5) == 0.125
    with pytest.raises(ValueError):
        VolumeCalculator.cube(-1)
    with pytest.raises(ValueError):
        VolumeCalculator.cube(0)

def test_sphere():
    assert VolumeCalculator.sphere(3) == pytest.approx(113.097, rel=1e-3)
    assert VolumeCalculator.sphere(0.5) == pytest.approx(0.5236, rel=1e-3)
    with pytest.raises(ValueError):
        VolumeCalculator.sphere(-1)
    with pytest.raises(ValueError):
        VolumeCalculator.sphere(0)

def test_cylinder():
    assert VolumeCalculator.cylinder(3, 5) == pytest.approx(141.372, rel=1e-3)
    assert VolumeCalculator.cylinder(0.5, 2) == pytest.approx(1.5708, rel=1e-3)
    with pytest.raises(ValueError):
        VolumeCalculator.cylinder(-1, 5)
    with pytest.raises(ValueError):
        VolumeCalculator.cylinder(3, -5)
    with pytest.raises(ValueError):
        VolumeCalculator.cylinder(0, 5)
    with pytest.raises(ValueError):
        VolumeCalculator.cylinder(3, 0)

def test_cone():
    assert VolumeCalculator.cone(3, 5) == pytest.approx(47.1239, rel=1e-3)
    assert VolumeCalculator.cone(0.5, 2) == pytest.approx(0.5236, rel=1e-3)
    with pytest.raises(ValueError):
        VolumeCalculator.cone(-1, 5)
    with pytest.raises(ValueError):
        VolumeCalculator.cone(3, -5)
    with pytest.raises(ValueError):
        VolumeCalculator.cone(0, 5)
    with pytest.raises(ValueError):
        VolumeCalculator.cone(3, 0)
