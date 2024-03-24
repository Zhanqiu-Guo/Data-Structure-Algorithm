def e_approx(n):
    sum = 0
    new = 1
    for i in range(1, n+2):
        sum += 1/(new)
        new = new*i
    return sum
