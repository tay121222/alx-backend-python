#!/usr/bin/env python3
"""Coroutine called async_comprehension that takes no arguments"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """write a coroutine called async_comprehension that takes no arguments
    then return the 10 random numbers"""
    return [value async for value in async_generator()]
