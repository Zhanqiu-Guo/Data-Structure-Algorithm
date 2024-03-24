def fibs(n):
    f0 = f1 = 1
    i = 0
    while i < n:
        yield f0
        f0, f1 = f1, f0 + f1
        i += 1

