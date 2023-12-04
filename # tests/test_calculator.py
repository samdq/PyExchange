# tests/test_calculator.py

from geometric_calculator.calculator import Calculator

def test_circle_area():
    assert Calculator.calculate_area('circle', 5) == 78.54

def test_rectangle_area():
    assert Calculator.calculate_area('rectangle', 4, 6) == 24

def test_triangle_area():
    assert Calculator.calculate_area('triangle', 3, 8) == 12
