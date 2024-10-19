import time
from functools import wraps

import numpy as np

def time_it(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {time.time()-start:.2f} s')

        return result
    return wrapper

def gmean(values: np.ndarray):
    values = values.astype(np.float64)
    result = 1

    for i in range(0, len(values)):
        result *= values[i] ** (1 / len(values))

    return result
