#!/usr/bin/env python3
"""Type annotated function"""
from typing import Mapping, TypeVar, Union, Optional, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Union[T, None]:
    """Type annotated function safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
