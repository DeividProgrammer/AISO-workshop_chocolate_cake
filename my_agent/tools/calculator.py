import math


def calculator(operation: str, a: float, b: float) -> str:
    """
    A calculator tool that performs arithmetic operations on two numbers.
    
    Supports the following operations:
    - 'add' or '+': Addition (a + b)
    - 'subtract' or '-': Subtraction (a - b)
    - 'multiply' or '*': Multiplication (a * b)
    - 'divide' or '/': Division (a / b) - handles division by zero
    - 'power' or '**' or '^': Exponentiation (a raised to power b)
    - 'modulo' or '%': Modulo operation (a mod b) - handles division by zero
    
    Args:
        operation: The arithmetic operation to perform
        a: The first number (float)
        b: The second number (float)
    
    Returns:
        A string containing the result of the operation or an error message
    
    Examples:
        calculator('add', 5, 3) -> "8.0"
        calculator('divide', 10, 2) -> "5.0"
        calculator('divide', 5, 0) -> "Error: Division by zero is undefined"
    """
    # Normalize operation to lowercase for case-insensitive matching
    op = operation.lower().strip()
    
    try:
        # Addition
        if op in ['add', '+', 'plus']:
            result = a + b
            
        # Subtraction
        elif op in ['subtract', '-', 'minus']:
            result = a - b
            
        # Multiplication
        elif op in ['multiply', '*', 'times', 'x']:
            result = a * b
            
        # Division
        elif op in ['divide', '/', 'div']:
            if b == 0:
                return "Error: Division by zero is undefined. Cannot divide by zero."
            result = a / b
            
        # Exponentiation
        elif op in ['power', '**', '^', 'pow', 'exponent']:
            # Handle edge cases for exponentiation
            if a == 0 and b < 0:
                return "Error: Cannot raise 0 to a negative power (division by zero)."
            try:
                result = a ** b
                # Check for overflow or invalid results
                if math.isinf(result):
                    return f"Error: Result is infinity (overflow). {a}^{b} is too large."
                if math.isnan(result):
                    return f"Error: Result is not a number. Invalid operation: {a}^{b}."
            except OverflowError:
                return f"Error: Overflow - {a}^{b} is too large to compute."
            
        # Modulo
        elif op in ['modulo', '%', 'mod', 'remainder']:
            if b == 0:
                return "Error: Modulo by zero is undefined. Cannot compute modulo with divisor of zero."
            result = a % b
            
        else:
            return f"Error: Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide, power, modulo."
        
        # Format result - remove unnecessary decimals for whole numbers
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        else:
            # Round to reasonable precision to avoid floating point artifacts
            return str(round(result, 10))
            
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"
