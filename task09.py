import functools


def to_format(format_='JSON'):
    import json
    from json2xml import json2xml
    from json2xml.utils import readfromstring
    import yaml

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if format_.upper() == 'XML':
                data = readfromstring(json.dumps(result))
                return json2xml.Json2xml(data).to_xml()
            elif format_.upper() == 'YAML':
                return yaml.dump(result)
            else:
                return json.dumps(result)
        return wrapper
    return decorator


@to_format()
def double_sum(a):
    return 2*sum(a)

@to_format('yaml')
def to_tuple(a, b, c=0, d=0):
    return (a, b, c, d)

@to_format('xml')
def to_dict(list1, list2):
    return dict(zip(list1, list2))

print(double_sum([1, 2, 3, 4, 5]))
print(to_tuple(1, 2))
print(to_dict([1, 2, 3], [3, 2, 1]))
