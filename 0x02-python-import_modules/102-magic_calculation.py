#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    print(f"a: {a}, b: {b}")

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

result = magic_calculation(5, 3)
print(f"Result: {result}")
