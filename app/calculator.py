class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from the first."""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide first number by the second."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b