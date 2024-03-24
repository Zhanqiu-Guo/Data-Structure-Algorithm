from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    length = 1
    for num in lst:
        stack.push(num)
    for i in range(1, len(lst)+1):
        length *= i
    for i in range(length):
        queue.enqueue([])
    for j in range(len(lst)):
        val = stack.pop()
        index = 0
        for i in range(1,length+1):
            temp_lst = queue.dequeue()
            temp_lst.insert(index,val)
            queue.enqueue(temp_lst)
            index = (index+1)%(j+1)
    queue.enqueue([])
    for j in range(length):
        for i in range(length-j-1):
            queue.enqueue(queue.dequeue())
        temp = queue.dequeue()
        queue.first().append(temp)
        queue.enqueue(queue.dequeue())
    return queue.dequeue()
