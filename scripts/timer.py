from time import perf_counter


def time_call(fn, *args, repeats=1, **kwargs):
    start = perf_counter()
    for _ in range(repeats):
        fn(*args, **kwargs)
    end = perf_counter()
    return (end - start) / repeats
