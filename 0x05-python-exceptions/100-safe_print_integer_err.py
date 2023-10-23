import sys

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError:
        sys.stderr.write("Exception: You have provided a non-integer value\n")
        return False

# Test the function with various inputs
value1 = 42
value2 = "hello"
value3 = "123"
value4 = 3.14

print("Printing integers:")
result1 = safe_print_integer_err(value1)  # Should print 42
print("Result 1:", result1)

print("Printing a non-integer string:")
result2 = safe_print_integer_err(value2)  # Should print an error message and return False
print("Result 2:", result2)

print("Printing a string that can be converted to an integer:")
result3 = safe_print_integer_err(value3)  # Should print 123
print("Result 3:", result3)

print("Printing a float:")
result4 = safe_print_integer_err(value4)  # Should print an error message and return False
print("Result 4:", result4)
