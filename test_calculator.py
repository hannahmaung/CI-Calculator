"""
Tests for calculator app
"""

import calculator 


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_mult(self):
        assert 8 == calculator.multiply(2, 4)
        
    def test_divide(self):
        assert 10 == calculator.divide(20, 2)
        

        