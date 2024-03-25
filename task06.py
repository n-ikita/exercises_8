import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(arg):
        result = func(arg)
        print(result)
    return wrapper


@decorator
def double_sum(a):
    return 2*sum(a)

double_sum([1, 2, 3, 4, 5])
print(double_sum.__name__)

