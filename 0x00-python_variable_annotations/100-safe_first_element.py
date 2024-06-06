#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a sequence of any type and returns its first element."""
from typing import Union, Any, Sequence
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of list if it exists."""
    if lst:
        return lst[0]
    else:
        return None