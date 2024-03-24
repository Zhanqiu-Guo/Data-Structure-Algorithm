def permutations(lst, low, high):
    if low == high:
        return [[1]]
    else:
        temp = permutations(lst,low,high-1)
        perlst = []
        for i in temp:
            for index in range(high+1):
                perm = i[:]
                perm.insert(index,lst[high])
                perlst.append(perm)
        return perlst

