# 0x00. Pascal's Triangle

This Python script generates Pascal's Triangle up to the nth row.

## Overview

Pascal's Triangle is a mathematical structure where each number is the sum of the two directly above it. This script provides a function that generates Pascal's Triangle up to a specified number of rows.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/mohdmuslim92/alx-interview.git
    cd alx-interview/0x00-pascal_triangle
    ```

2. Run the provided `0-main.py` file to see an example usage of the function:

    ```bash
    ./0-main.py
    ```

    This script uses `pascal_triangle` function to generate Pascal's Triangle up to the 5th row and prints it.

## Function Explanation

The `pascal_triangle` function takes an integer `n` as input and returns a list of lists representing Pascal's Triangle up to the `n`th row.

## Example

The provided `0-main.py` file contains an example of how to use the function and print the generated triangle:

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Output

```bash
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
