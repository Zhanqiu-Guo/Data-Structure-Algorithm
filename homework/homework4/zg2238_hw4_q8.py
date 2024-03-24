def flat_list(nested_lst, low, high):
    if low > high:
        return []
    else:
        lst = flat_list(nested_lst,low,high-1)
        temp = nested_lst[high]
        if isinstance(temp,list):
            k = flat_list(temp,0,len(temp)-1)
            lst.extend(k)
        else:
            lst.append(nested_lst[high])
        return lst

