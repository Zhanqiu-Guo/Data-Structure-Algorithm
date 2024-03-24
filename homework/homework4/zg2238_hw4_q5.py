def count_lowercase(s, low, high):
    if low == high:
        if s[low]==s[low].lower():
            return 1
        return 0
    else:
        count = count_lowercase(s,low+1,high)
        if s[low]==s[low].lower():
            count+=1
        return count

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low]==s[low].lower():
            return False
        return True
    else:
        flag = is_number_of_lowercase_even(s,low+1,high)
        if s[low]==s[low].lower():
            if flag == True:
                flag = False
            else:
                flag = True
        return flag

