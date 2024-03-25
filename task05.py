from functools import reduce
from math import sqrt
a, b, c = map(int, input().split())

square_multiply = reduce(lambda x1, x2: x1*x2,
                         filter(lambda x: (x%c == 0 and sqrt(x) == int(sqrt(x))),
                                range(a, b+1)))
print(square_multiply)
