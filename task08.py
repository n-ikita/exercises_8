import functools
import datetime

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            with open('log.txt', 'a') as log_file:
                log_file.write(str(datetime.datetime.now())[:-7] + '  ->Exception: ' + str(exc)+'\n')
        return func(*args, **kwargs)
    return wrapper

@logger
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))

