from ArrayStack import ArrayStack

def eval_postfix(exp_str):
    operator = '+-*/'
    exp_lst = exp_str.split(' ')
    args_stack = ArrayStack()
    for i in range(len(exp_lst)):
        token = exp_lst[i]
        if token not in operator:
            if token in dict.keys():
                token = dict[token]
            args_stack.push(float(token))
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

flag = True
dict = {}
while flag:
    exp_str = input('--> ')
    if exp_str == 'done()':
        flag = False
    elif '=' in exp_str:
        exp_lst = exp_str.split(' = ')
        var = exp_lst[0]
        exp_str = exp_lst[1]
        value = str(eval_postfix(exp_str))
        print(var)
        dict[var] = value
    else:
        value = str(eval_postfix(exp_str))
        length = len(value)-1
        while length >= 1:
            if value[length] != '0' and value[length] == '.':
                value = value[:length]
                length = 0
            elif value[length] != '0':
                value = value[:length+1]
                length = 0
            length -= 1
        print(value)








