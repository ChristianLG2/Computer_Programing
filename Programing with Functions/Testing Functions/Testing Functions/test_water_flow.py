
from pytest import approx
import pytest
from water_flow import (water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction)


def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.1)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    test_data = [
        (0.048692, 0, 0.018, 1.75, 0, 0.001),
        (0.048692, 200, 0, 1.75, 0, 0.001),
        (0.048692, 200, 0.018, 0, 0, 0.001),
        (0.048692, 200, 0.018, 1.75, -113.008, 0.001),
        (0.048692, 200, 0.018, 1.65, -100.462, 0.001),
        (0.28687, 1000, 0.013, 1.65, -61.576, 0.001),
        (0.28687, 1800.75, 0.013, 1.65, -110.884, 0.001),
    ]

    for diameter, length, friction, velocity, expected, tolerance in test_data:
        assert pressure_loss_from_pipe(diameter, length, friction, velocity) == approx(expected, abs=tolerance)

def test_pressure_loss_from_fittings():
    test_data = [
        (0, 3, 0, 0.001),
        (1.65, 0, 0, 0.001),
        (1.65, 2, -0.109, 0.001),
        (1.75, 2, -0.122, 0.001),
        (1.75, 5, -0.306, 0.001)
    ]

    for velocity, fittings, expected, tolerance in test_data:
        assert pressure_loss_from_fittings(velocity, fittings) == approx(expected, abs=tolerance)

def test_reynolds_number():
    test_data = [
        (0.048692, 0, 0, 1),
        (0.048692, 1.65, 80069, 1),
        (0.048692, 1.75, 84922, 1),
        (0.28687, 1.65, 471729, 1),
        (0.28687, 1.75, 500318, 1),
    ]

    for diameter, velocity, expected, tolerance in test_data:
        assert reynolds_number(diameter, velocity) == approx(expected, abs=tolerance)


def test_pressure_loss_from_pipe_reduction():
    test_data = [
        (0.28687, 0, 1, 0.048692, 0, 0.001),
        (0.28687, 1.65, 471729, 0.048692, -163.744, 0.001),
        (0.28687, 1.75, 500318, 0.048692, -184.182, 0.001),
    ]

    for larger_diameter, velocity, reynolds, smaller_diameter, expected, tolerance in test_data:
        result = pressure_loss_from_pipe_reduction(larger_diameter, velocity, reynolds, smaller_diameter)
        if result != approx(expected, abs=tolerance):
            raise Exception(f"Test data: larger_diameter={larger_diameter}, velocity={velocity}, reynolds={reynolds}, smaller_diameter={smaller_diameter}\nExpected: {expected}, Result: {result}, Difference: {abs(expected - result)}")
        
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
