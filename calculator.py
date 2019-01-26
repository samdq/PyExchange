# geometric_calculator/calculator.py
from .shapes import Circle, Rectangle, Triangle

class Calculator:
    @staticmethod
    def calculate_area(shape, *args):
        if shape.lower() == 'circle':
            return Circle(*args).area()
        elif shape.lower() == 'rectangle':
            return Rectangle(*args).area()

