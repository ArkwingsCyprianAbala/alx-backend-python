#!/usr/bin/env python3
"""
Type-annotated function type_check
that takes an element and returns its type.
"""
from typing import Union, Any, Tuple, List, TypeVar
T = TypeVar('T')


def type_check(element: Any) -> Tuple[Union[T, None], Union[T, None]]:
    """Return tuple of element and its type."""
    return (element, type(element))
