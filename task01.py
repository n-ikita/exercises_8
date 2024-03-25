s = input()
i, j = map(int, input().split())

upper_letter_list = list(filter(lambda x: (x != x.lower()), s[i-1:j]))
print(len(upper_letter_list))
