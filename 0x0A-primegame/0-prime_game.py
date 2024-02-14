#!/usr/bin/python3
"""
Prime Game Module

This module provides a function to determine the winner of a prime game.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game for each round.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n, where n is the limit of consecutive
                     integers for each round.

    Returns:
        str: The name of the player that won the most rounds. If the winner
             cannot be determined, returns None.
    """
    def generate_primes(n):
        """
        Generate prime numbers up to a given limit.

        Args:
            n (int): The upper limit for prime number generation.

        Returns:
            list: A list of prime numbers up to the given limit.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

    def round_winner(n):
        """
        Determine the winner of a single round of the prime game.

        Args:
            n (int): The limit of consecutive integers for the round.

        Returns:
            str: The name of the winner of the round.
        """
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = []
    for n in nums:
        winners.append(round_winner(n))
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
