s = c = 0
while (n := int(input())) != 0:
    s += n
    c += 1
print(s // c if c else 0)
