#!/usr/bin/env python3
'''
Regular function to create and return a list of asyncio.Task
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Regular function that creates and returns a list of asyncio.Tasks for task_wait_random(max_delay).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)