import math
def factors(num):
    i = 0
    while i <= math.sqrt(num):
        i += 1
        if num%i == 0:
            yield i
    i -= 1
    while i >= 2:
        i -= 1
        if num%i == 0:
            yield num//i
