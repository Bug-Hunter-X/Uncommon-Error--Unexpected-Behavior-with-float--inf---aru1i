def function_with_uncommon_error(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return float('inf')  # This can lead to unexpected behavior
    else:
        return x / y

result = function_with_uncommon_error(10, 0)