def sum_to(n):
    if n <= 0:
        return 0
    else:
        sum = sum_to(n-1)
        sum += n
        return sum

def product_evens(n):
    if n <= 0:
        return 1
    else:
        product = product_evens(n-2)
        product *= n
    return product

def find_max(lst, low, high):
    if low == high:
        if lst[low] > lst[0]:
            return lst[low]
        else:
            return lst[0] # base case
    prev = find_max(lst,low+1,high)
    if prev > lst[low]:
        return prev
    return lst[low]

def is_palindrome(str, low, high):
    if low == high or low+1 == high:
        if str[low] == str[high] :
            return True
        else:
            return False
    else:
        flag = is_palindrome(str,low+1,high-1)
        if str[low] == str[high]:
            return flag and True
        return flag and False
print(is_palindrome('acbcca', 0, 5))
print(is_palindrome('acbbca', 0, 5))
def binary_search(lst, low, high, val):
    found=False
    int=None
    while found==False and low<=high:
        mid=(low+high)//2
        if lst[mid]==val:
            found=True
            int=mid
        elif val<lst[mid]:
            high=mid-1
        elif val>lst[mid]:
            low=mid+1
    return int

def vc_count(word, low, high):
    vowel = 0
    word = word.lower()
    def vc_help(word,low,high):
        if low == high:
            if word[low] in 'aeiou':
                return 1
            else:
                return 0
        else:
            vowel = vc_help(word, low+1, high)
            if word[low] in 'aeiou':
                return vowel+1
            else:
                return vowel
    vowel = vc_help(word,low,high)
    return (vowel, len(word)-vowel)
