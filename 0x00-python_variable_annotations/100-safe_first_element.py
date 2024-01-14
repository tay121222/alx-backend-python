#!/usr/bin/env python3
"""duck-typed annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Ducked-typed annotation function that takes a sequence (1st) and
    returns the first element if the sequence is not empty"""
    if lst:
        return lst[0]
    else:
        return None
