#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    print(f"a: {a}, b: {b}")  # Add this line for debugging

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Call the function for debugging purposes
result = magic_calculation(5, 10)
print(f"Result: {result}")
