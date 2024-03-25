a, b, c, d = map(int, input().split())

num_list = list(filter(lambda x: (x % c == 0
                                           and x % d == 0), range(a, b + 1)))
print(sum(num_list))
