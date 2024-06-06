#!/usr/bin/env python3
"""
Type-annotated function make_multiplier which takes a float
multiplier as argument
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies float by multiplier."""
    def multiply(num: float) -> float:
        """Return product of multiplier and num."""
        return multiplier * num
    return multiply
