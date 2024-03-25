import functools

def to_json(func):
    import json
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

@to_json
def double_sum(a):
    return 2*sum(a)

@to_json
def to_tuple(a, b, c=0, d=0):
    return (a, b, c, d)

@to_json
def to_dict(list1, list2):
    return dict(zip(list1, list2))

print(double_sum([1, 2, 3, 4, 5]))
print(to_tuple(1, 2))
print(to_dict([1, 2, 3], [3, 2, 1]))
