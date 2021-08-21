

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(funct):
    def wrapper():
        before_funct_time = time.time()
        funct()
        after_funct_time = time.time()
        delta_funct = after_funct_time - before_funct_time
        print('function time: ', delta_funct)
    return wrapper
    # fast_function()
    # after_fast_time = time.time()
    # delta_fast = after_fast_time - after_slow_time
    # print('fast function: ', delta_fast)

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


def slow_function():
    for i in range(100000000):
        i * i

# speed_calc_decorator(fast_function)
fast_function()
# speed_calc_decorator(slow_function)
slow_function()
