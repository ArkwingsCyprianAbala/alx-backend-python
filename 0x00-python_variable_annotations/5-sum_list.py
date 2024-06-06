#!/usr/bin/env python3
"""
Type-annotated function sum_list which takes
list input_list of floats as argument
returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of list of floats."""
    return sum(input_list)
