def appearances(s, low, high):
    if low == high:
        return {s[high]:1}
    else:
        dict = appearances(s,low,high-1)
        dict[s[high]] = dict.get(s[high], 0)+1
        return dict

