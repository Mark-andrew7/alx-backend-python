#!/usr/bin/env python3
'''
Coroutine that measures the runtime of executing async_comprehension four times in parallel.
'''

import asyncio
import time
from typing import List
from random import uniform

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime of executing async_comprehension four times in parallel.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time