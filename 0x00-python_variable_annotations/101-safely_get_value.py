#!/usr/bin/env python3
"""Type-annotated function safely_get_value that takes a dict, a key and an optional default value and returns the value of the key if it exists, otherwise None."""
from typing import Union, Any, TypeVar, Mapping
T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return value of key in dictionary if it exists, otherwise None."""
    if key in dct:
        return dct[key]
    else:
        return default