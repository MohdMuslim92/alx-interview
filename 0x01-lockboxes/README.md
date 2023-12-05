# 0x01. Lockboxes

This Python module checks if all the boxes in a set of boxes can be opened.

## Overview

This module provides a method, `canUnlockAll`, to determine if all the boxes in a set of boxes can be opened. It uses a traversal algorithm to simulate opening boxes using keys.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/Lockboxes.git
    ```

2. Example usage in your script:

    ```python
    #!/usr/bin/python3

    from lockboxes import canUnlockAll

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False
    ```

    This demonstrates the usage of the `canUnlockAll` function with different sets of boxes and their respective outputs.

## Function Explanation

The `canUnlockAll` function takes a list of lists (`boxes`) as input, where each inner list represents a box. Each box may contain keys to other boxes. It returns `True` if all boxes can be opened, otherwise `False`.

## Example

The provided script `main.py` contains examples of how to use the `canUnlockAll` function with various sets of boxes and their corresponding outputs.

```python
#!/usr/bin/python3

from lockboxes import canUnlockAll

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
