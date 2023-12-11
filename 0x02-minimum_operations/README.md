# 0x02-minimum_operations

This directory contains a Python script that calculates the minimum number of operations needed to achieve a specific number of characters using the "Copy All" and "Paste" operations in a text file.

## Overview

The `0-minoperations.py` script implements a dynamic programming approach to calculate the fewest number of operations required to result in exactly `n` characters in the file, using only two available operations: "Copy All" and "Paste".

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/alx-interview.git
    ```

2. Navigate to the `0x02-minimum_operations` directory:

    ```bash
    cd alx-interview/0x02-minimum_operations
    ```

3. Run the provided `0-main.py` file to test the `minOperations` function:

    ```bash
    ./0-main.py
    ```

    Example usage:

    ```python
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
    ```

## Function Explanation

The `minOperations` function takes an integer `n` as input and calculates the minimum number of operations needed to achieve exactly `n` characters in the file using "Copy All" and "Paste" operations.

## Example

The provided `0-main.py` file contains examples of how to use the `minOperations` function with different values of `n` and their corresponding minimum operations.

```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
