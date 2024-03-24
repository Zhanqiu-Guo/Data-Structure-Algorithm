def two_sum(srt_lst, target):
    i = j = len(srt_lst)//2
    while j < len(srt_lst) and i >= 0:
        if srt_lst[i] + srt_lst[j] == target:
            return (i,j)
        elif srt_lst[i] + srt_lst[j] > target:
            i -= 1
            if j < len(srt_lst) and i >= 0:
                if srt_lst[i] > target/2:
                    j -= 1
        elif srt_lst[i] + srt_lst[j] < target:
            j += 1
            if j < len(srt_lst) and i >= 0:
                if srt_lst[j] < target/2:
                    i += 1
    return None

lst1 = [1,2,4,5,13,30]
print(two_sum(lst1,7))





