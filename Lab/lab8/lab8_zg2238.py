#1
'''
10
4
'''
#2
'''
does nothing
name: nothing
'''
#3
'''
find the minimum value in the stack
name: min_val
'''
#4
'''
3 4 * 10 -
+ * 5 5 / 10 2
+ / - 10 2 4 8 | (10 - 2) / 4 + 8 | 10
6 * 3 + 8 * 4 | 6 3 * 8 4 * + | 50
- + * 8 2 4 + 3 6 | 8 2 * 4 + 3 6 + - | 11
'''
#5
'''
3
4
'''
#6
'''
removing even integers and reverse odd in the queue
name: reverse_odd_queue
'''
#7
'''
return False if the input_str is not symmetric, else return True
name: is_symmetric
'''
from ArrayStack import ArrayStack
def stack_sum(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        sum = stack_sum(s)
        sum += val
        s.push(val)
        return sum

def eval_prefix(exp_str):
    operator = '+-*/'
    exp_lst = exp_str.split(' ')
    args_stack = ArrayStack()
    for i in range(len(exp_lst)-1,-1,-1):
        token = exp_lst[i]
        if token not in operator:
            args_stack.push(int(token))
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if token == '+':
                res = arg1 + arg2
            elif token == '-':
                res = arg1 - arg2
            elif token == '*':
                res = arg1 * arg2
            elif token == '/':
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)
    return args_stack.pop()

def flatten_lst(lst):
    stack = ArrayStack()
    while len(lst) != 0:
        val = lst.pop()
        if isinstance(val,lst):
            lst.extend(val)
        else:
            stack.push(val)
    while not stack.is_empty():
        lst.append(stack.pop())

def stack_sort(s):
    helper = ArrayStack()
    while not s.is_empty():
        temp = s.pop()
        while not helper.is_empty() and temp<helper.top():
            s.push(helper.pop())
        if helper.is_empty() or temp > helper.pop():
            helper.push(temp)
    while not helper.is_empty():
        s.push(helper.pop())

