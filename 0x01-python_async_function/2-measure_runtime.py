#!/usr/bin/env python3
'''
Measure runtime of wait_n coroutine and return average time per task
'''

import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n  # Importing wait_n from previous file

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time of wait_n(n, max_delay) and return average time per task.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    
    return average_time