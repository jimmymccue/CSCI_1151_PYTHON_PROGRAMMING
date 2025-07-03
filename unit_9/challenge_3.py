# ZeroDivisionError is raised when you attempt to divide a number
# by zero, which is mathematically undefined.
# 
# Instructions:
# 1. Capture the ZeroDivisionError.
# 2. if exception is thrown return None
# 3. else return answer
# 4. Update documentation and the typehints so it is accurate for the function


def divide(a: float, b: float)  -> float | None:
    """
    Divides two numbers, handling division by zero.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        The result of a / b, or None if division by zero.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    return a / b
    




result = divide(10, 0)
    


