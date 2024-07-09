#!/usr/bin/env python3
'''
Regular function to create and return an asyncio.Task
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that creates and returns an asyncio.Task for wait_random(max_delay).
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task