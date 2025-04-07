for i in range(8, 10):
    for j in range(1, i + 1):
        num_str = ''.join(str(k) for k in range(1, j + 1))
        result = int(num_str) * i + j
        print(f"{num_str} * {i} + {j} = {result}")

print()

for i in range(1, 10):
    num_str = '1' * i
    result = int(num_str) * int(num_str)
    print(f"{num_str} * {num_str} = {result}")
