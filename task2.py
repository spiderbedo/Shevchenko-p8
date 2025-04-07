best = count = 0
while (n := int(input())) != -1:
    count += 1
    if n > best: best = n
print(best, count)
