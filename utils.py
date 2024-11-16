import time
from functools import wraps

import numpy as np

from constants import DEBUG_MODE, MAX_PIXEL_VALUE

def time_it(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        if DEBUG_MODE:
            print(f'time taken by {func.__name__} is {time.time()-start:.3f} s')

        return result
    return wrapper

def gmean(values: np.ndarray):
    values = values.astype(np.float64)
    result = 1

    for i in range(0, len(values)):
        result *= values[i] ** (1 / len(values))

    return result

def clip(x: int, max: int = MAX_PIXEL_VALUE, min: int = 0) -> int:
    if x >= max:
        return max
    if x <= min:
        return min
    return x 