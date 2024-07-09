#!/usr/bin/env python3
'''
Asynchronous coroutine that spawns n instances of wait_random with specified max_delay
'''

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random  # Importing wait_random from previous file

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns n instances of wait_random with specified max_delay.
    Returns list of all the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    results = await asyncio.gather(*tasks)
    delays.extend(results)
    
    return sorted(delays)