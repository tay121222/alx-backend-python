#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier that takes a
    float multiplier as argument and returns a function"""

    def mul_multiplier(x: float) -> float:
        """function that multiplies a float by multiplier"""
        return x * multiplier
    return mul_multiplier
