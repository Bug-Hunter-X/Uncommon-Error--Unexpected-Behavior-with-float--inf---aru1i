def function_with_improved_error_handling(x, y):
    if x == 0:
        return 0
    elif y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    else:
        return x / y

try:
    result = function_with_improved_error_handling(10, 0)
except ZeroDivisionError as e:
    print("Error:", e)