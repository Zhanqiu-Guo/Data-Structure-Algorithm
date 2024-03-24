def find_duplicates(lst):
    repeat = [i for i in range(len(lst))]               #O(n)
    for elem in lst:                                    #O(n)
        if repeat[elem] != None and repeat[elem] != 0:  ##O(1)
            repeat[elem] = None                         ##O(1)
        elif repeat[elem] == None:                      ##O(1)
            repeat[elem] = 0                            ##O(1)
            repeat.append(elem)                         ##O(1)
    return repeat[len(lst):]                            #O(n)

#Time complexity: O(n)

def remove_all_evens(lst):
    fei = 0
    for i in range(len(lst)):
        if lst[i]%2 == 1:
            lst[fei],lst[i] = lst[i],lst[fei]
            fei += 1
    while fei < len(lst):
        lst.pop()
    return lst
print(remove_all_evens([3, 3, 5, 2, 16, 13,21]))

