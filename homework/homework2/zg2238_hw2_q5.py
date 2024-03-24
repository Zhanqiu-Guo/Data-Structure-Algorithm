def split_parity(lst):
    i = j = k = 0
    while i <= len(lst)-1:
        if lst[i]%2==0:
            k = i
            while i+j <= len(lst)-1:
                if lst[i+j]%2!=0:
                    lst[k], lst[i+j]=lst[i+j],lst[k]
                    k += 1
                j += 1
            i = i+j
        i += 1

