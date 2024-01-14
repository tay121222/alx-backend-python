#!/usr/bin/env python3
"""Type annotated function"""
from typing import Mapping, TypeVar, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, Any]:
    """Type annotated function safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
