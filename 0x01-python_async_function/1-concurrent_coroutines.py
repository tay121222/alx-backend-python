#!/usr/bin/env python3
"""async routine called wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async routine called wait_n that takes in 2 int arguments"""
    list_output = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    list_output = sorted(await asyncio.gather(*tasks))
    return list_output
