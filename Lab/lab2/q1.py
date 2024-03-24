'''[(-2)**x for x in range(8)]

my_str = 'Python'
print([my_str[x] for x in range(-len(my_str),len(my_str))])

def one():
    i = 0
    str = ''
    while i < 7:
        str = str + '1'
        yield str
        i += 1
lst = []
for curr in one():
    lst.append(curr)
print(lst)

def powers_of_two(n):
    i = 0
    while i < n:
        yield 2 ** i
        i += 1
for curr in powers_of_two(6):
    print(curr)
'''

class Polynomial:
    def __init__(self, coefficients = [0]):
        self.coefficients = coefficients.reverse()
    def __add__(self, other):
        length = max(len(self.coefficients),len(other.coefficients))
        lst = [0 for x in range(length)]
        for j in range(len(self.coefficients)):
            lst[j] += self.coefficients[j]
        for j in range(len(other.coefficients)):
            lst[j] += other.coefficients[j]
        return Polynomial(lst)
    def __call__(self, param):




