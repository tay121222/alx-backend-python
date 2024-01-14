#!/usr/bin/env python3
"""Type annotated function"""
from typing import Mapping, TypeVar, Union, Any, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Type annotated function safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
