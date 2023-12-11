#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to achieve 'n' characters
by using dynamic programming.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve 'n'
    characters.

    Args:
    - n (int): The target number of characters.

    Returns:
    - int: The minimum number of operations required.
    """

    if n <= 1:
        return 0

    # Create a list to store the minimum operations needed for each count of
    # characters
    operations_needed = [0] * (n + 1)

    # Iterate through the range of 2 to n to calculate minimum operations for
    # each count
    for i in range(2, n + 1):
        # Initialize the number of operations for i characters to i
        # (maximum number of operations)
        operations_needed[i] = i

        # Iterate through possible factors j of i to find the minimum
        # operations
        for j in range(2, i // 2 + 1):
            # Check if j is a factor of i
            if i % j == 0:
                # Update operations_needed[i] with the minimum operations found
                # so far
                operations_needed[i] = min(
                        operations_needed[i], operations_needed[j] + i // j)

    # Return the minimum operations needed to achieve n characters
    return operations_needed[n]
