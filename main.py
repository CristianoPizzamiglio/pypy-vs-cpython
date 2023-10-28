from __future__ import annotations

import random
from time import perf_counter
from typing import Iterator


def compute_primes(integer: int) -> Iterator[int]:
    """
    Compute all the prime numbers smaller or equal than the integer.

    Sieve of Eratosthenes.

    Parameters
    ----------
    integer : int

    Returns
    -------
    Iterator[int]

    """
    primes_ = set()
    for i in range(2, integer + 1):
        if i not in primes_:
            yield i
            primes_.update(range(i * i, integer + 1, i))


def estimate_pi(iterations: int = 10_000_000) -> float:
    """
    Estimate py using the Monte Carlo method.

    Parameters
    ----------
    iterations

    Returns
    -------
    float

    """
    circle_point_count = 0
    square_point_count = 0
    for _ in range(iterations):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        distance = x**2 + y**2

        if distance <= 1:
            circle_point_count += 1
        square_point_count += 1

    return 4 * circle_point_count / square_point_count


if __name__ == "__main__":
    for _ in range(10):
        t0 = perf_counter()
        primes = list(compute_primes(10_000_000))
        elapsed = perf_counter() - t0
        print(elapsed)
