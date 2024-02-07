# 0x09. Island Perimeter

This directory contains solutions and exercises related to the Island Perimeter problem.

## Problem Statement

Create a function `island_perimeter(grid)` that returns the perimeter of the island described in the given grid:

- `grid` is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - Grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Usage

To test the `island_perimeter` function:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/alx-interview.git
    ```

2. Navigate to the `0x09-island_perimeter` directory:

    ```bash
    cd alx-interview/0x09-island_perimeter
    ```

3. Run the `0-main.py` script:

    ```bash
    ./0-main.py
    ```

    This script tests the `island_perimeter` function with a sample grid and prints the calculated perimeter.
