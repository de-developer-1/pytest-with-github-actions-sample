"""Tests for the calculator module."""
import pytest

from app.calculator import add, subtract, multiply, divide

def test_add():
    """Test addition functionality."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction functionality."""
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    """Test multiplication functionality."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    """Test division functionality."""
    assert divide(6, 3) == 2.0
    assert divide(-6, 2) == -3.0
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    """Test division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)