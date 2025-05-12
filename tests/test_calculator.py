import pytest
from app.calculator import Calculator

class TestCalculator:
    def test_add(self):
        """Test addition method."""
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction method."""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(-1, 1) == -2
        assert Calculator.subtract(0, 0) == 0
    
    def test_multiply(self):
        """Test multiplication method."""
        assert Calculator.multiply(2, 3) == 6
        assert Calculator.multiply(-2, 3) == -6
        assert Calculator.multiply(0, 5) == 0
    
    def test_divide(self):
        """Test division method."""
        assert Calculator.divide(6, 3) == 2
        assert Calculator.divide(-6, 2) == -3
        assert Calculator.divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Calculator.divide(5, 0)