def remove_all(lst, value):
    i = 0                                                   #O(1)
    count = 0                                               #O(1)
    try:
        while i < len(lst):                                 #O(n)
            if lst[i] == value:                             ##O(1)
                j = 1                                       ##O(1)
                while lst[i + j] != value:                  ##O(1) iteration times=seperation of two consecutive values in lst
                    j += 1                                  ##O(1)
                lst[i-count:i+j-1-count] = lst[i+1:i+j]     ##O(1)
                count += 1                                  ##O(1)
                i += j - 1                ##O(1) reduce iteration time for outer while loop=iteration time in inner while loop
            i += 1                                          ##O(1)
    except IndexError:
        if lst[-1] == value:                                ##O(1)
            count += 1                                      ##O(1)
    finally:
        for n in range(count):                              ##O(n)
            lst.pop()                                       ##O(1)
        return lst

#Time complexity=O(n)



def test(n):
    if n==1:
        return [2]
    else:
        lst=test(n-1)
        lst.append(2**n)
        return lst
print(test(4))
