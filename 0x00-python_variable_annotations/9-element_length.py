#!/usr/bin/env python3
"""Type-annotated function element_length which takes a list mxd_lst of integers and floats and returns their sum as a float."""
from typing import List, Union
def element_length(lst: List[Union[int, float]]) -> List[int]:
    """Return list of integers representing lengths of elements."""
    return [len(str(i)) for i in lst]