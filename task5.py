n = int(input())
count = 0
for num in range(2, n + 1):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s == num:
        count += 1
print(count)
