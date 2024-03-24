def findChange(lst01):
    i = len(lst01)//2
    n = 2
    while len(lst01)//n != 1:
        if lst01[i] == 0:
            i = i + len(lst01)//(2**n)
        elif lst01[i] == 1:
            i = i - len(lst01)//(2**n)
        n += 1
    if lst01[i] == 1:
        return i
    else:
        return i+1
