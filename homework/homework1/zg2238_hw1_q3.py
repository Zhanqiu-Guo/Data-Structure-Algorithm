def square_sum(n):
    sum = num = 0
    while num < n:
        sum += num**2
        num += 1
    return sum

sum([x**2 for x in range(n)])

def odd_square_sum(n):
    sum = num = 0
    while num < n:
        if num % 2 != 0:
            sum += num**2
        num += 1
    return sum

sum([x**2 for x in range(n) if x % 2 != 0])

print(type([1]))
