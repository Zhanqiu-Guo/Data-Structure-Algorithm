def shift(lst, k, direction = 'left'):
    n = 0
    if direction == 'left':
        while k > n:
            lst.append(lst.pop(0))
            n += 1
    elif direction == 'right':
        while k > n:
            lst.insert(0,lst.pop())
            n += 1
    return lst
