def calculator(num1, num2, operation):
    """Apply an arithmetic operator to two numbers."""
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    raise ValueError(f"Unsupported operation: {operation}")