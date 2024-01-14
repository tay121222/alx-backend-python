#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their
    sum as a float"""
    ans: float = 0
    for i in mxd_lst:
        ans = ans + i
    return ans
