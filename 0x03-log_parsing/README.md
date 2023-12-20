# 0x03-log_parsing

This directory contains a script `0-stats.py` that reads logs from standard input (stdin) line by line and computes various metrics based on the input format.

## Overview

The `0-stats.py` script processes log lines in a specific format:

Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

The script calculates metrics after every 10 lines or upon keyboard interruption (CTRL + C) and prints the following statistics from the beginning:

- Total file size: `<total size>` (the sum of all previous `<file size>`)
- Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
    - Status codes printed in ascending order

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/mohdmuslim92/alx-interview.git
    ```

2. Navigate to the `0x03-log_parsing` directory:

    ```bash
    cd alx-interview/0x03-log_parsing
    ```

3. Generate logs using the provided `0-generator.py` script:

    ```bash
    ./0-generator.py | ./0-stats.py
    ```

    This will simulate log generation and processing based on the specified input format.

## Files

- `0-stats.py`: Python script that computes metrics based on log lines read from stdin.
- `0-generator.py`: Python script to generate sample log lines for testing `0-stats.py`.
