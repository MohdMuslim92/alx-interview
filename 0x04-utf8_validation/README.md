# 0x04. UTF-8 Validation

This directory contains a method `validUTF8` that determines if a given dataset represents a valid UTF-8 encoding.

## Overview

The `validUTF8` function checks whether a given list of integers, representing bytes of data, conforms to the rules of a valid UTF-8 encoding.

### Functionality

- **Prototype**: `def validUTF8(data)`
- **Return**: True if data is a valid UTF-8 encoding, else return False
- **Character Length**: A character in UTF-8 can be 1 to 4 bytes long
- **Data Set Format**: The data set is represented by a list of integers
- **Handling**: Each integer represents 1 byte of data, considering only the 8 least significant bits of each integer

## Usage

To test the `validUTF8` function, utilize the provided `0-main.py` script:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/utf-8-validation.git
    ```

2. Navigate to the `utf-8-validation` directory:

    ```bash
    cd utf-8-validation
    ```

3. Run the `0-main.py` file to test the `validUTF8` function with different datasets:

    ```bash
    ./0-main.py
    ```

    This script tests the `validUTF8` function with various input datasets and validates the output.

## Files

- `0-validate_utf8.py`: Python script containing the `validUTF8` function.
- `0-main.py`: Example usage testing the `validUTF8` function.
