def fib_recursive(n):
    """ Returns the Finabocci's value for 'n' using recursion.
    
    Args:
        n (int): number of interactions.
    Returns:
        int: Fibonacci's value.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
def fib_dictionary(n, d={0:1,1:1}):
    """ Returns the Finabocci's value for 'n' using dictionary.
    
    Args:
        n (int): number of interactions.
        d (dict): dictionary that store values.
    Returns:
        int: Fibonacci's value.
    """
    if n in d:
        return d[n]
    else:
        answer = fib_dictionary(n-1) + fib_dictionary(n-2)
        d[n] = answer
        return answer

# testing
for fib in [fib_recursive, fib_dictionary]:
    print(fib)
    assert fib(0) ==  1, "value is incorrect"
    assert fib(1) ==  1, "value is incorrect"
    assert fib(2) ==  2, "value is incorrect"
    assert fib(3) ==  3, "value is incorrect"
    assert fib(4) ==  5, "value is incorrect"
    assert fib(5) ==  8, "value is incorrect"
    assert fib(6) == 13, "value is incorrect"
    assert fib(7) == 21, "value is incorrect"