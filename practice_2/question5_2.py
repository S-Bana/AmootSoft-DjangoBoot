def generate_fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a Fibonacci sequence up to the nth term.

    This function uses recursion to generate the Fibonacci sequence.
    It returns a list containing the first n terms of the sequence.

    Args:
        n (int): The number of terms to generate in the sequence.

    Returns:
        list[int]: A list containing the first n terms of the Fibonacci sequence.
    """
    # Base cases
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    # Recursive case
    else:
        # Recursively generate the sequence for n-1 terms
        fib = generate_fibonacci_sequence(n - 1)
        # Add the next Fibonacci number (sum of the last two numbers)
        fib.append(fib[-1] + fib[-2])
        return fib


# Example usage
num_terms = int(input('Enter the number of Fibonacci terms to generate: '))
result = generate_fibonacci_sequence(num_terms)
print(f"The first {num_terms} terms of the Fibonacci sequence are:")
print(result)
