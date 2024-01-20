#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10"""
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
