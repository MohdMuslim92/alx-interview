# 0x0A. Prime Game

This program determines the winner of a game played by Maria and Ben based on selecting prime numbers from a set of consecutive integers.

## Overview

Maria and Ben play a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. They remove the chosen prime number and its multiples from the set. The player who cannot make a move loses the game. This program determines the winner of each round based on the given parameters.

### Functionality

- **Prototype**: `def isWinner(x, nums)`
- **Return**: Name of the player that won the most rounds. If the winner cannot be determined, return None.
- **Constraints**:
    - x is the number of rounds, and nums is an array of n.
    - You can assume n and x will not be larger than 10000.
    - You cannot import any packages in this task.

### Example

Given x = 3 and nums = [4, 5, 1]:

1. First round: 4
    - Maria picks 2 and removes 2, 4, leaving 1, 3
    - Ben picks 3 and removes 3, leaving 1
    - Ben wins because there are no prime numbers left for Maria to choose.

2. Second round: 5
    - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    - Ben picks 3 and removes 3, leaving 1, 5
    - Maria picks 5 and removes 5, leaving 1
    - Maria wins because there are no prime numbers left for Ben to choose.

3. Third round: 1
    - Ben wins because there are no prime numbers for Maria to choose.

Result: Ben has the most wins.

## Usage

Clone this repository to access the code files and run the main script with appropriate arguments to test the functionality.

```bash
git clone https://github.com/mohdmuslim92/alx-interview.git
cd alx-interview/0x0A-primegame
./main_0.py
