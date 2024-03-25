a, b, c, d = map(int, input().split())

num_count = sum(map(lambda x: 1 if x%c!=0 and x%10 == d else 0, range(a ,b+1)))
print(num_count)