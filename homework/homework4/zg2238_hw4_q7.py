def split_by_sign(lst, low, high):
    if low == high:
        return
    else:
        dict = split_by_sign(lst,low+1,high)
        if lst[low] > 0:
            lst.append(lst.pop(low))
