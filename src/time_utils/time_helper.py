import time

def human_readable_time() -> str:
    return time.ctime()[11:19]
