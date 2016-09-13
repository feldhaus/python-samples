def fibonacci(n):
    """ Returns the Finabocci's value for 'n'.
    
    Args:
        n (int): number of interactions.
    Returns:
        int: Fibonacci's value.
    """
	if n < 3:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(1) ==  1, "value is incorrect"
assert fibonacci(2) ==  2, "value is incorrect"
assert fibonacci(3) ==  3, "value is incorrect"
assert fibonacci(4) ==  5, "value is incorrect"
assert fibonacci(5) ==  8, "value is incorrect"
assert fibonacci(6) == 13, "value is incorrect"
assert fibonacci(7) == 21, "value is incorrect"