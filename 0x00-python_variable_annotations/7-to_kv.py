#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes a string k
and an int OR float v as arguments
returns a tuple. The first element of the tuple is the string k.
The second element is the square of the int OR float v.
The return type is a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of string and square of int OR float."""
    return (k, v * v)
