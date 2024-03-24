def reverse_list(lst, low = None, high = None):
    for i in range(low, low + (high-low)//2+1):
        lst[i], lst[high+low-i] = lst[high+low-i], lst[i]
    return lst

print(reverse_list( [1, 2, 3, 4, 5, 6],low = 0, high = 5))
print(reverse_list( [1, 2, 3, 4, 5, 6],low = 1, high = 3))

def move_zeros(nums):
    for i in range(len(nums)-1):
        if nums[i] == 0:
            j = i + 1
            while nums[j] == 0 and j < len(nums)-1:
                j += 1
            nums[i],nums[j]=nums[j],nums[i]
            i = j
    return nums

print(move_zeros( [0, 1, 0, 3, 13, 0,5]))

def shift(lst, k):
    reverse_list(lst, 0, len(lst)-k-1)
    reverse_list(lst, len(lst)-k,len(lst)-1)
    reverse_list(lst, 0, len(lst)-1)
    return lst

print(shift([1, 2, 3, 4, 5, 6], 2))


def max_subarry(nums, k):
    max_sum = 0
    for i in range(0,len(nums)-len(nums)//k+1):
        if sum(nums[i:i+3])>max_sum:
            max_sum = sum(nums[i:i+3])
    return max_sum

print(max_subarry( [1,12,-5,-6,50,3],2))

