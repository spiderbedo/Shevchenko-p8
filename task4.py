x = int(input())
s = 0
for i in range(1, x + 1):
    s += i
    print(' + '.join(map(str, range(1, i + 1))), '=', s)
