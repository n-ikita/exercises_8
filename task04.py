import json

json_str = input()  # ex: [["a", 3], ["b", 0], ["c", 1], ["d", -4], ["e", 9]]

tuples_list = json.loads(json_str)
tuples_list.sort(key=lambda x: x[1], reverse=True)

print(tuples_list)
