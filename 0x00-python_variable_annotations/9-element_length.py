#!/usr/bin/env python3
"""function element_length that takes an iterable of sequences"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function element_length that takes an iterable of sequences"""
    return [(i, len(i)) for i in lst]
