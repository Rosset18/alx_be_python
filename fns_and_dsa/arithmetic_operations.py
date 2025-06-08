def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    
    Parameters:
    - num1 (float): First number.
    - num2 (float): Second number.
    - operation (str): Operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.
    
    Returns:
    - float or str: The result of the operation, or a message for division by zero or invalid operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

