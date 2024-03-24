def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        min = list_min(lst,low,high-1)
        if lst[high] < min:
            min = lst[high]
        return min
