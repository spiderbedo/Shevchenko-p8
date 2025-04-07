N = int(input())

def is_perfect(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

for num in range(2, N + 1):
    if is_perfect(num):
        print(num)
