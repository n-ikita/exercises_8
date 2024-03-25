import functools
import time


def timer(time_completing=1, quantity=5, time_for_quantity=2):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            time0 = float(time.time())
            with open('tlog.txt', 'r') as file:
                time_log = file.readlines()

            with open('tlog.txt', 'w') as file:

                while len(time_log) >= quantity:
                    time_log.pop(0)
                time_log.append(str(time0))
                if float(time_log[-1]) - float(time_log[0]) < time_for_quantity and len(time_log) >= quantity:
                    raise RuntimeError('too many calls')
                else:
                    for _ in range(len(time_log)):
                        time_log[i] = time_log[i].replace('\n', '') + '\n'
                    file.writelines(time_log)

            result = func(*args, **kwargs)
            time1 = float(time.time())
            if time1 - time0 > time_completing:
                raise TimeoutError(f'prepared for {time1 - time0} sec. instead of {time_completing}')
            return result
        return wrapper
    return decorator


@timer()
def waiting(t):
    print('good night')
    time.sleep(t)
    print('good morning')


for i in range(6):
    waiting(0.02)
