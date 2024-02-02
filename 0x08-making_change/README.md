# 0x08. Making Change

This program, `0-making_change.py`, determines the fewest number of coins needed to meet a given total amount, given a pile of coins of different values.

## Overview

The `makeChange` function in `0-making_change.py` calculates the fewest number of coins needed to meet a specified total. The program handles various edge cases, including checking if the total is 0 or less and verifying if the given coins can make up the total amount.

### Functionality

- **Prototype**: `def makeChange(coins, total)`
- **Return**: Returns the fewest number of coins needed to meet the total.
    - If the total is 0 or less, the function returns 0.
    - If the total cannot be met by any combination of available coins, the function returns -1.
- **Input**: `coins` is a list of values representing the denominations of coins available.
- **Assumptions**:
    - The value of a coin will always be an integer greater than 0.
    - The program assumes you have an infinite number of each denomination of coin in the list.

## Usage

To test the `makeChange` function, use the provided `0-main.py` script:

1. Clone this repository:

    ```bash
    git clone https://github.com/mohdmuslim92/alx-interview.git
    ```

2. Navigate to the `0x08-making_change` directory:

    ```bash
    cd alx-interview/0x08-making_change
    ```

3. Run the program with different coin values and total amounts:

    ```bash
    ./0-main.py
    ```

    This script tests the `makeChange` function with various input scenarios and validates the output.
